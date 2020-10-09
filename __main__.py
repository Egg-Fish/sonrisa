from sonrisa.functions import formatting, processing
import matplotlib.pyplot as plt
import numpy as np

import sys

def main(path):

    ChatData = formatting.ChatData(path)
    p = ChatData.search(time ="1111")

    print(ChatData.search(time = "1111"))
    print(processing.average_messages_per_day(p, sender="Amar"))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        path = input("Enter a path: ")
    elif len(sys.argv) == 2:
        path = sys.argv[1]
    main(path)

