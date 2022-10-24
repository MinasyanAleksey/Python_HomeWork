# ----- ЗАДАЧА 3 -----
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def create_list(k):
    formula = str()
    import random
    for i in range(1, k+1):
        s = str(random.randint(0, 100)) + '*' + 'x' + '^' + str(i)
        formula += s + ' + '
        #form = formula[:-3]
        form = formula[:-3] + ' = 0'
    return form

try:
    k = int(input("Введите размерность натуральной степени К: "))
except ValueError as ex:
    print('Введите целое число')
    print(ex)

formula = create_list(k)

data = open('file.txt', 'w')
data.write(formula)
data.close

#print(create_list(k))