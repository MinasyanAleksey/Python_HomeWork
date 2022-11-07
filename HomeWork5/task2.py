# ----- ЗАДАЧА 2 -----
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# 1 -------- Читаем данные из файла enter_file.txt для последующей кодировки -------

with open('enter_file.txt', 'r') as inf:
    data = inf.read()

def rle_encode(data):       # --- Модуль сжатия данных ---
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data: return '' 
    for char in data: 
        if char != prev_char:  
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding 

encoded_val = rle_encode(data)
print(encoded_val)

# 2 -------- Записываем закодированние данные в файл exit_file.txt -------

with open('exit_file.txt', 'w') as inf:
    inf.write(encoded_val)

# 3 -------- Читаем закодированные данные из файла exit_file.txt для последующей разкодировки -------

with open('exit_file.txt', 'r') as inf:
    data = inf.read()

def rle_decode(data):       # --- Модуль восстановления данных ---
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 
    return decode

decoded_val = rle_decode(data)
print(decoded_val)