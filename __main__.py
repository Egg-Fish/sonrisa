from sonrisa.functions import formatting, processing
import matplotlib.pyplot as plt
import numpy as np

import sys

def main(path):
    # This is the testing branch
    # if you see this, you are free to test

    ChatData = formatting.ChatData(path)
    print(ChatData.search(date=294))

if __name__ == "__main__":
    main(sys.argv[1])

