
#Завдання 3. Написати функцію, що приймає два параметри: два додатні
#числа, а повертає boolean значення чи перше число ділиться на друге без остачі.
#Передбачити вивід помилки (Exception), коли введено хоча б одне від’ємне
#число
import sys
import input

a = input.a
b = input.b

def div(a,b):
	result = False
	if a % b == 0:
		result = True
	return result
print(div(a,b))