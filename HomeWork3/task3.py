# ----- ЗАДАЧА 3 -----
# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def create_list(m):
    list = []
    import random
    for i in range(m):
        list.append(round(random.uniform(0.99, 10), 2))
       
    return list

def selection_decimal(list):
    list2 = []
    for i in list:
        if i%1 !=0:
            list2.append(round(i%1, 2))
    return list2

try:
    num = int(input('Введите размерность списка: '))
except ValueError as ex:
    print('Введите целое число!')
    exit(ex)
list = create_list(num)
print(list)
print()
dec = selection_decimal(list)
print(f'Максимальная дробная часть - {max(dec)}')
print()
print(f'Минимальная дробная часть - {min(dec)}')
print()
print(f'Разница между максимальным и минимальным значением дробной части элементов = {round(max(dec) - min(dec), 2)}')
