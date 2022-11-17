import model
import logs as l
import view as v

def button_click():
    choice = v.user_choice()
    valid = False
    while not valid:
        if choice == 1:
            value1 = input('Введите пример для вычисления: ')
            value1 = value1.replace(' ', '')
            print()
            result1 = model.rational_numbers(value1)
            l.rational_logger(value1, result1)
            valid = True
        if choice == 2:
            value2 = input('Введите комплексное выражение, пример: (a + bj) + (c + dj): ')
            print()
            result2 = model.complex_numbers(value2)
            l.complex_logger(value2,result2)
            valid = True
        if choice == 3:
            exit()
    
    