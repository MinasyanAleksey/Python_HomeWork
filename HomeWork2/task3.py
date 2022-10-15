# ----- ЗАДАЧА 3 -----
# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

def find_str(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    count = 0
    if len1 >= len2:
        for i in range(0, len1 - len2 + 1):
            if s1[i:len2+i] == s2:
                count += 1
        print(f'Количество повторений строки 2 в строке 1: {count}')
    else:
        for i in range(0, len2 - len1 + 1):
            if s2[i:len1+i] == s1:
                count += 1
        print(f'Количество повторений строки 1 в строке 2: {count}')


st1 = input('Введите строку 1: ')
st2 = input('Введите строку 2: ')

find_str(st1, st2)