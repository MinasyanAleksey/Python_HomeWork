# ----- ЗАДАЧА 4 -----
# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

try:
    def calculator():
        num1 = float(input('Введите первое число - '))
        operator = (input('Введите тип операции (+, -, /, *, mod, pow, div) - '))
        num2 = float(input('Введите второе число - '))

        if operator == '+':
            res = num1 + num2
            print(f'{num1} + {num2} = {res}')
        elif operator == '-':
            res = num1 - num2
            print(f'{num1} - {num2} = {res}')
        elif operator == '*':
            res = num1 * num2
            print(f'{num1} * {num2} = {res}') 
        elif operator == 'pow':
            res = num1 ** num2
            print(f'{num1} ** {num2} = {res}')
        elif num2 != 0:
            if operator == '/':
                res = num1 / num2
                print(f'{num1} / {num2} = {res}')
            elif operator == 'mod':
                res = num1 % num2
                print(f'{num1} % {num2} = {res}')
            elif operator == 'div':
                res = num1 // num2
                print(f'{num1} // {num2} = {res}')
        else: print("Divine for zero.")

    calculator()
except:
    print('ОШИБКА! Введено не число!!! - Введите число!')