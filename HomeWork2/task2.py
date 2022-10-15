# ----- ЗАДАЧА 2 -----
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] -> (1, 1*2, 1*2*3, 1*2*3*4)

def find_multiplications(num):
    mult = 1
    list = []
    for i in range(1, num + 1):
        mult *= i
        list.append(mult)
    return list

try:
    num = int(input('Введите число:'))
except ValueError:
    print('ОШИБКА! Введено не число!!! - Введите число!')

list_mult = find_multiplications(num)
print(list_mult)