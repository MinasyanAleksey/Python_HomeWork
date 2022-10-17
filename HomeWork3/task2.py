# ----- ЗАДАЧА 2 -----
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def create_list(m):
    list = []
    import random
    for i in range(m):
        list.append(random.randint(1, 9))
       
    return list

def multiplicate_of_elements(arr):
    list2 = []
    l = len(arr)//2 + 1 
    if len(arr) % 2 != 0:
        for i in range(l):
            list2.append(arr[i]*arr[len(arr)-i-1])
    else:
        for i in range(l-1):
            list2.append(arr[i]*arr[len(arr)-i-1])
        
    return list2

num = int(input('Введите размерность списка: '))
list = create_list(num)
print(list)
print()
print(f'Произведение пар чисел - {multiplicate_of_elements(list)}')