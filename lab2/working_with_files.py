#Завдання 2. Створити файл a.txt із віршем Тараса Шевченка «Cадок
#вишневий коло хати» (Забезпечити правильність закриття файлу, роботи з
#дескриптором файлів). Створити файл b1.txt, в який записати кожен #парний
#рядок із файлу а, всі слова записати у верхньому регістрі. Створити #файл b2.txt,
#в який записати всі непарні рядки, всі слова повинні бути записаними у
#нижньому регістрі.

import os
import sys
with open("a.txt", "r") as f, open("b1.txt", "w") as even, open("b2.txt", "w") as odd:
	newLine = ""
	count = 0;
	for i in f:
		count+=1
		if count%2 == 0:
   			even.write(i.upper())
		else:
   			odd.write(i.lower())

			