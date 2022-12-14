# ----- ЗАДАЧА 4 -----
# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def chenge_dec(n):
    res = ""
    while n != 0:
        res = str(n % 2) + res
        n = n // 2
    
    return res

try:
    num = int(input('Введите число: '))
except ValueError as ex:
    print('Введите целое число!')
    exit(ex)
dec = chenge_dec(num)
print(f'Число {num} в десятичном выражении - {dec}')