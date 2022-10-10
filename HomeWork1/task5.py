# ----- ЗАДАЧА 5 -----
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

try:
    def create_2d_list(m, n):
        list_2d = []
        import random
        for i in range(m):
            list = []
            for j in range(n):
                list.append(random.randint(1, 9)) # Генерация списка случайными числами от 1 до 9(в данном примере). Диапазон можно менять.
            list_2d.append(list)
        return list_2d

    def show_2d_list(arr_2d):
        for i in range(len(arr_2d)):
            for j in range(len(arr_2d[i])):
                print(arr_2d[i][j], end = ' ')
            print()

    def sorted_2d_list(arr_2d):
        for i in range(len(arr_2d)):
            arr_2d.sort()
            for j in range(len(arr_2d[i])):
                arr_2d[i].sort()
        return arr_2d

    rows = int(input('Введите колличество строк: '))
    columns = int(input('Введите колличество столбцов: '))

    list_2d = create_2d_list(rows, columns)

    show_2d_list(list_2d)
    print()
    show_2d_list(sorted_2d_list(list_2d))
except:
    print('ОШИБКА! Введено не число!!! - Введите число!')