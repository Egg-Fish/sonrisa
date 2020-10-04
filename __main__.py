from sonrisa.functions import formatting, processing

path = "C:\\Users\\Egie\\Desktop\\Projects\\SonrisaProjects\\Text\\Amar.txt"

data = formatting.ChatData(path)

print(data.search(year="2019"))