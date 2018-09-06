# Завдання 5. Дано масив
# ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
# Написати програму, яка перетворить заданий масив з кількома рівнями
# вкладеності (масив з неоднотипними елементами) в масив з одним рівнем
# вкладеності. Тобто програма має вивести масив, з такими елементами:
# ['a', 'c', 1, 3, 'f', 7, 4, '4', {'lalala': 111}]
# При написанні програми передбачити можливість введення іншого
# масиву з іншими даними в якості контрольного прикладу для перевірки
# коректності роботи розробленого алгоритму.
input_list = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

out_list = []
def iterate_nested_list(in_list):
    for i in in_list:
          if isinstance(i,list):
                iterate_nested_list(i)
          else:
                out_list.append(i)

iterate_nested_list(input_list)
print(out_list)