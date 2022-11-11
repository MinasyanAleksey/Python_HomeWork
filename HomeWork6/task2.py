# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример: 2+2 => 4;
#         1+2*3 => 7;
#         1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7;
#         (1+2)*3 => 9;

task = input('Введите пример: ')
#task = '11+2*3-1'
#task = '17 - 5 * 6 / 3 - 2 + 4 / 2'
#task = '9 - 2 * 3 / 3 - 2 + 4 / 2'
#task = '17 - 5 * 6 - 2 + 4 / 2'
#task = '1 - 2*3'

task = task.replace(' ', '')
print(task)

def mult(task):
    a = task.index("*")
    answer = int(task[a-1]) * int(task[a+1])
    if len(task) == 3:
        task = str(answer)
    else:
        task = task[0:a-1] + str(answer) + task[a+2:]
    return task

def div(task):
    a = task.index("/")
    answer = int(task[a-1]) // int(task[a+1])
    if len(task) == 3:
        task = str(answer)
    else:
        task = task[0:a-1] + str(answer) + task[a+2:]
    return task

def sum(task):
    a = task.index("+")
    answer = int(task[a-1]) + int(task[a+1])
    if len(task) == 3:
        task = str(answer)
    else:
        task = task[0:a-1] + str(answer) + task[a+2:]
    return task

def diff(task):
    a = task.index("-")
    answer = int(task[a-1]) - int(task[a+1])
    if len(task) == 3:
        task = str(answer)
    else:
        task = task[0:a-1] + str(answer) + task[a+2:]
    return task

if '*' in task:
    counter = task.count('*')
    if counter > 1:
        for i in range(counter):
            task = mult(task)
    else: 
        task = mult(task)
    #print(task)

if '/' in task:
    counter = task.count('/')
    if counter > 1:
        for i in range(counter):
            task = div(task)
    else: 
        task = div(task)
    #print(task)

if '+' in task:
    counter = task.count('+')
    if counter > 1:
        for i in range(counter):
            task = sum(task)
    else: 
        task = sum(task)
    #print(task)

if '-' in task:
    counter = task.count('-')
    if counter > 1:
        for i in range(counter):
            task = diff(task)
    else: 
        task = diff(task)
    print(task)
