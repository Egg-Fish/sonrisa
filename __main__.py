from sonrisa.functions import formatting, processing
import matplotlib.pyplot as plt
import numpy as np

import sys

def main(path):

    ChatData = formatting.ChatData(path)
    print(ChatData.data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        path = input("Enter a path: ")
    elif len(sys.argv) == 2:
        path = sys.argv[1]
    main(path)

