# ----- ЗАДАЧА 4 -----
# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

def create_list(dim):
    arr = [0]*dim
    for i in range(dim):
        try:    
            arr[i] = float(input(f'Введите координату {i + 1}: '))
        except:
            print('Введите вещественное число')

    return arr

def find_distance(a, b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i])**2
    return sum**0.5

try:    
    dim = int(input(f'Введите мерность пространства: '))
except:
    print('Введите целое число')

print()
print('Координаты первой точки: ')
a = create_list(dim)
print()
print('Координаты второй точки: ')
b = create_list(dim)

dist = find_distance(a, b)
print(f'Расстояние между двумя точками - {dist}')