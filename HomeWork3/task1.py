# ----- ЗАДАЧА 1 -----
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_list(m):
    list = []
    import random
    for i in range(m):
        list.append(random.randint(1, 9))
       
    return list

def sum_of_elements(arr):
    sum = 0
    for i in range(1, len(arr), 2):
        sum += arr[i]
    return sum

try:
    num = int(input('Введите размерность списка: '))
except ValueError as ex:
    print('Введите целое число!')
    exit(ex)

list = create_list(num)
print(list)
print()
print(f'Сумма элементов находящихся на нечетных позициях = {sum_of_elements(list)}')