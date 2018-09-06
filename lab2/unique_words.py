#Завдання 3. Створити файл c.xml (згідно з стандартами), записати в нього
#всі унікальні слова та кількість їх вживання у тексті, використовуючи файл а.txt
#із завдання 2.
import sys

f =  open("a.txt", "r") 
c = open("c.xml", "w")
all_words = []
for i in f:
	all_words.append(i.split(" "))
print(all_words)