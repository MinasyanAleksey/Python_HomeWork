# ----- ЗАДАЧА 1 ----- 
# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def convert_to_int(n):  
    temp = n - int(n)  
    if temp != 0:  
        multiplier = 1  
        while not (n*multiplier).is_integer():  
            multiplier = 10 * multiplier
            number = int(n * multiplier)
        return number

def find_sum(number):
    sum = 0
    while (number != 0):
        sum = sum + number % 10
        number //= 10
    return sum

try:
    num = float(input('Введите число:'))
except ValueError:
    print('ОШИБКА! Введено не число!!! - Введите число!')

num1 = float(num).is_integer()
number = convert_to_int(num)

if num1 == True:
    num = int(num)
    result = int(find_sum(num))
    print(f'Сумма цифр числа {num} = {result}')
else:
    result = find_sum(number)
    print(f'Сумма цифр числа {num} = {result}')