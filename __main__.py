from sonrisa.functions import formatting, processing
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Users\\Egie\\Desktop\\Projects\\SonrisaProjects\\Text\\C1.txt"

data = formatting.ChatData(path)

q = processing.message_frequency(data.data, message = ["simp","lol"])
print(q)
q.plot("pie")
plt.show()
