from collections import Counter
import pandas as pd
import numpy as np

def message_frequency(df, n = 0, message = None):
    data = df["Message"].values
    words= []

    for m in data:
        words.extend([word for word in m.split()])

    data = pd.Series(words).value_counts()

    if n != 0 and message != None:
        raise Exception("n and message cannot co-exist")

    if n != 0:
        data = data.iloc[:n]

    if message != None:
        if type(message) == list:
            data = data.loc[np.isin(data.index, message)]

        else:
            data = data.loc[data.index == message]

    return data

def total_messages_by_sender(df, sender = None):
    if type(sender) == list:
        return df.loc[np.isin(df["Sender"], sender), "Sender"].value_counts()
    
    elif type(sender) == str:
        return df.loc[df["Sender"] == sender, "Sender"].value_counts()

    return df["Sender"].value_counts()