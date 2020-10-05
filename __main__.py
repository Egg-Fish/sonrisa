from sonrisa.functions import formatting, processing
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Users\\Egie\\Desktop\\Projects\\SonrisaProjects\\Text\\Amar.txt"

data = formatting.ChatData(path)

freq = processing.message_frequency(data, 20)

print(freq)