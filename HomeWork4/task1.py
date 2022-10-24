# ----- ЗАДАЧА 1 -----
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

try:
    num = int(input("Введите число: "))
except ValueError as ex:
    print('Введите целое число')
    print(ex)

i = 2 # первое простое число
mult = []
old = num
while i <= num:
    if num % i == 0:
        mult.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {mult}")