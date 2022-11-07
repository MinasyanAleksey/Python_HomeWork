# ----- ЗАДАЧА 3 -----
# Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

text = input("Введите текст через пробел: ")
find_text = "абв"
list = [i for i in text.split() if find_text not in i]
print(f'Результат: {" ".join(list)}')