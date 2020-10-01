import datetime
import re

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
    line = line.split(maxsplit=5)
    date = line[0][:-1]
    date = date_to_day_number(date)
    time = convert_12_to_24(line[1],line[2])
    sender = line[4][:-1]
    message = line[5]

    return [date, time, sender, message]

class ChatData():
    def __init__(self, path):
        path = path.replace("\\","/")
        f = open(path,encoding="utf-8").readlines()

        data = []
        queue = f[0].rstrip()
        for i in range(1,len(f)):

            line = f[i].rstrip()
            if re.search(r'^[0-9]+/[0-9]+/[0-9]+',line):
                data.append(queue)
                queue = line
            else:
                print(i)
                queue = queue + line

        self.data = data

            
        

