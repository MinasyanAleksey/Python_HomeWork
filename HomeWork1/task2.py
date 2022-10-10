# ----- ЗАДАЧА 2 -----
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

try:
    x = int(input("Введите значение x: "))
    y = int(input("Введите значение y: "))
    z = int(input("Введите значение z: "))

    left_part = not (x or y or z)
    right_part = not x and not y and not z

    if left_part == right_part:
        print("Высказывание верно")
    else:
        print("Высказывание ложно")
except:
    print("Введите число!")