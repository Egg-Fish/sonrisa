from sonrisa.functions import formatting, processing
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Users\\Egie\\Desktop\\Projects\\SonrisaProjects\\Text\\GC1.txt"

data = formatting.ChatData(path)

print(data.search(date="18/2/19",year="2019"))

