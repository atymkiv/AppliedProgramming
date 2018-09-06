# Завдання 4. Використовуючи функцію із попереднього завдання створити
# нову функцію, яка приймає два параметри – два числа, та повертає масив
# простих чисел у цьому відрізку або видає помилку ‘NoSimpleDigits’, коли таких
# немає.
import sys
import input

a = input.a
b = input.b 

def primal(st, en):
    primal_numbers = []
    for x in range(st, en):
        for n in range(2, x):
            if x % n == 0:
                break;
        else:
            primal_numbers.append(x)
    if len(primal_numbers) == 0:
        raise Exception('NoSimpleDigits')
    return primal_numbers

print(primal(a,b))