from datetime import datetime as dt

def rational_logger(value, result1):
    time = dt.now().strftime("%c")
    with open('logbook.txt', 'a', encoding='utf-8') as file:
        file.write(str(time) + '- Текущая сессия с рациональными числами\n ')
        file.write(' Вычисляем следующее: ' + str(value) + '\n')
        file.write(' Результат вычисления = ' + str(result1) + '\n')

def complex_logger(value,result2):
    time = dt.now().strftime("%c")
    with open('logbook.txt', 'a', encoding='utf-8') as file:
        file.write(str(time) + '- Текущая сессия с комплексными числами\n ')
        file.write(' Вычисляем следующее: ' + str(value) + '\n')
        file.write(' Результат вычисления = ' + str(result2) + '\n')