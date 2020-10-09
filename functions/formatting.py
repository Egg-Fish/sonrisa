import datetime
import re
import pandas as pd
from collections import Counter

def convert_12_to_24(time, period):
    x = time.split(":")
    hour = int(x[0])
    minute = x[1]
    
    if (hour not in range(0,13) or
        int(minute) not in range(0,61) or 
        period not in ["am", "pm"]):
        # Validation
        raise Exception("timeConvert: Invalid Format (Input: {}, {})".format(time,period))

    if period == "pm" and hour != 12:
        hour = hour + 12

    if period == "am" and hour == 12:
        hour = 0

    return str("0" + str(hour) + minute)[-4:] # extra 0 for 3 digit, AM timings (e.g 2:12 am -> 0212)

def date_to_day_number(date):
    x = date.split("/")
    day = x[0]
    month = x[1]
    year = "20" + x[2]
    date = datetime.datetime(int(year),int(month),int(day))
    day_number = (date - datetime.datetime(date.year, 1, 1)).days

    return day_number

def separate_categories(line):
    line = line.split(maxsplit=4)
    date = line[0][:-1]
    date = date_to_day_number(date)
    year = "20" + line[0][-3:-1]
    time = convert_12_to_24(line[1],line[2])
    
    sender_and_msg = line[4].split(":",maxsplit=1) # Message can contain ":" inside
    #print(sender_and_msg)
    if len(sender_and_msg) == 1:
        sender_and_msg = sender_and_msg[0].split(maxsplit=1)
        

    sender = sender_and_msg[0].strip()
    message = sender_and_msg[1].strip()


    return [date, year, time, sender, message]

def message_valid(data):
    if type(data) == list:
        message = data[4]
        sender = data[3]
    if type(data) == str:
        message = data
        sender = "egg"
    
    if (message != "<Media omitted>" and
        message != "You deleted this message" and
        message != "This message was deleted" and
        sender != "Messages" and
        re.search(r'security code changed', message) == None and
        re.search(r'changed the subject', message) == None and
        re.search(r'changed the group description', message) == None and
        re.search(r"changed this group's icon", message) == None and
        re.search(r'Messages and calls are end-to-end encrypted.', message) == None and
        re.search(r'created group', message) == None and
        re.search(r'added you', message) == None and
        re.search(r'^\d\d\d\d \d\d\d\d added [a-zA-Z0-9\w+()]+$', message) == None):
        # these are auto-generated messages by WhatsApp
        return True
    elif re.search(r'created group', message) != None:
        chat_name = message.rsplit("group")[-1].strip().strip("\"")
        return chat_name
    elif re.search(r'changed the subject', message) != None:
        chat_name = message.rsplit("to")[-1].strip().strip("\"")
        return chat_name
    else:
        return False

def strip_emoji(data):
    if type(data) == list:
        message = data[4]
    if type(data) == str:
        message = data

    final = ""
    for char in message:
        if re.search(r'[a-z-A-Z0-9!@#$%^&*(),.?"\':{}|<>\w\s]{1}', char):
            final = final + char

    if type(data) == list:
        data[4] = final.strip()
        return data

    if type(data) == str:
        return final.strip()
    



class ChatData():
    def __init__(self, path):

        self.data = None
        self.senders = None
        self.chat_name = None

        path = path.replace("\\","/")
        
        f = open(path,encoding="utf-8-sig").readlines()

        data = []
        queue = f[0].rstrip()
        for i in range(1,len(f)):

            line = f[i].rstrip()

            if re.search(r'^[0-9]+/[0-9]+/[0-9]+', line):
                p = separate_categories(queue)
                if message_valid(p):
                    if type(message_valid(p)) == str:
                        self.chat_name = message_valid(p)
                    else:
                        p = strip_emoji(p)
                        if p[4].strip():
                            data.append(p)
                    
                queue = line

            else:
                queue = queue + " " + line

        p = separate_categories(queue)
        if message_valid(p):
            p = strip_emoji(p)
            if p[4].strip():
                data.append(p)
        

        senders = [x[3] for x in data]
        senders = Counter(senders)
        if len(senders.keys()) == 2:
            chat_name = list(senders.keys())
            chat_name.remove("egg")
            self.chat_name = chat_name[0]

        self.senders = dict(senders)

        data = pd.DataFrame(data,columns=["Day", "Year", "Time", "Sender", "Message"])
        self.data = data

    def search(self, 
            date = None,
            year = None, 
            time = None, 
            sender = None, 
            message = None):
        
        if type(date) == str:
            date = date_to_day_number(date)

        data = self.data
        

        if date != None:
            data = data.loc[data["Day"] == date]

        if year != None:
            data = data.loc[data["Year"] == year]

        if time != None:
            data = data.loc[data["Time"] == time]
            
        if sender != None:
            data = data.loc[data["Sender"] == sender]
        
        if message != None:
            data = data.loc[ [re.search(message, x) != None for x in data["Message"]] ]
            # bool array made by for .. in .. genrator to check if message is present as a 
            # substring in each message of Data. JIC I forget what this is for :P
        
        return data




            
        


