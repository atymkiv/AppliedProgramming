a = int(input('Введіть перше число:'))
b = int(input('Введіть друге число:'))
if a < 0 or b < 0:
    raise Exception('Ви ввели від\'ємне число')