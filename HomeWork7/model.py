import re

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

# ---------- Работа с рациональными числами ----------

def rational_numbers(data):
    if '*' in data:
        counter = data.count('*')
        if counter > 1:
            for i in range(counter):
                data = mult(data)
        else: 
            data = mult(data)
    #print(data)

    if '/' in data:
        counter = data.count('/')
        if counter > 1:
            for i in range(counter):
                data = div(data)
        else: 
            data = div(data)
    #print(data)

    if '+' in data:
        counter = data.count('+')
        if counter > 1:
            for i in range(counter):
                data = sum(data)
        else: 
            data = sum(data)
    #print(data)

    if '-' in data:
        counter = data.count('-')
        if counter > 1:
            for i in range(counter):
                data = diff(data)
        else: 
            data = diff(data)
    print(f'Результат вычисления = {data}')
    return data

# ---------- Работа с комплексными числами ----------
x = ''
y = ''
def complex_numbers(data):
    data = data.replace(' ', '')
    result = re.split(r'[()]', data)
    global x
    global y
    
    x = complex(result[1])
    action = result[2]
    y = complex(result[3])

    if action == '+':
        answer = eval('x + y')
    if action == '-':
        answer = eval('x - y')
    if action == '*':
        answer = eval('x * y')
    if action == '/':
        answer = eval('x / y')
    
    print(f'Результат вычисления = {answer}')
    return answer