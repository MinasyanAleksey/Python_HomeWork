# ----- ЗАДАЧА 5 -----
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место 
# и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.

def create_2d_list(m, n):
    list_2d = []
    import random
    for i in range(m):
        list = []
        for j in range(n):
            list.append(random.randint(11, 99))
        list_2d.append(list)
    return list_2d

def show_2d_list(arr_2d):
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            print(arr_2d[i][j], end = ' ')
        print()

def sorted_2d_list(arr_2d):
    import random
    for i in range(len(arr_2d)):
        random.shuffle(arr_2d)
        for j in range(len(arr_2d[i])):
            random.shuffle(arr_2d[i])
    print(f'Колличество текущих итераций - {i+j}')
    print()       
    return arr_2d

try:
    rows = int(input('Введите колличество строк: '))
    columns = int(input('Введите колличество столбцов: '))
except ValueError as ex:
    print('Введите целое число!')
    exit(ex)

list_2d = create_2d_list(rows, columns)

show_2d_list(list_2d)
print()
print(f'Колличество итераций не должно быть больше {(rows*columns)//2}')
print()
show_2d_list(sorted_2d_list(list_2d))