# ----- ЗАДАЧА 2 -----
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def create_first_list(num):
    list = []
    import random
    for i in range(num):
        list.append(random.randint(1, 9))
    return list

try:
    num = int(input("Введите размер последовательности: "))
except ValueError as ex:
    print('Введите целое число')
    print(ex)

sequence = create_first_list(num)
list2 = list(set(sequence))
print()
print(f'Задана следующая последовательность - {sequence}')
print()
print(f'Список неповторяющихся элементов исходной последовательности - {list2}')