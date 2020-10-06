from sonrisa.functions import formatting, processing
import matplotlib.pyplot as plt
import numpy as np

import sys

def main(path):

    ChatData = formatting.ChatData(path)
    print(ChatData.data)

if __name__ == "__main__":
    main(sys.argv[1])

