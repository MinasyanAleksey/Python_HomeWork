# ----- ЗАДАЧА 5 - необязательная ----
# Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.

# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]
# Рекомендация на каникулы - посмотреть библиотеку EasyGUI, БД SQLite.

def create_list():
    list = []
    print('Заполните список числами!')
    print('Чтобы закончить ввод, отправьте пустое значение!')
    try:
        while (value := input('Введите число: ')) != '':
            list.append(int(value))
    except ValueError as error:
        print(f'Введите целое число! - {error}')
    return list

def find_sequence(list):
    min_value = min(list)
    for i in list:
        if (min_value + 1) in list:
            min_value += 1
    list2 = [min(list), min_value]

    return list2

print('Найдем максимальную последовательность вашего списка!')
new_list = create_list()
print(f'Исходный список: \n{new_list}')
result = find_sequence(new_list)
print(f'Максимальная последовательность элементов: \n{result}')