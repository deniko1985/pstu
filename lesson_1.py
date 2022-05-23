# 1. Сумму ряда 0 - 88888888
k = 0
print ('А теперь посчитаем')
# Начало цикла счета
for i in range (0, 88888889):
    k += i
# Вывод результата на экран
print (k, end = '')

# 1.1. Как первое задание, но с дополнением - возможностью пользовательского ввода данных.
# Вводим данные для подсчета
print ('Посчитаем сумму ряда чисел введенного пользователем')
start = int(input('Введите число начала ряда: '))
finish = int(input('Введите число конца ряда: '))
step = int(input('Введите число шага: '))
finish += 1 # так как функция range не включает в себя последнее число
k = 0
if start < 0 or finish <= 0 or step <= 0:
    print ('Нельзя вводить отрицательные значения')
else:
# Начало цикла счета
    print ('А теперь посчитаем: ')
    for i in range (start, finish, step):
        k += i
# Вывод результата на экран
    print (k, end = '')

# 2. Cреднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]
row = [3, 4, 56, 100, 2, 2, 3]
new_row: int = 0
index = 0
j = 0
for i in row:
    new_row += row[index]
    index += 1
    j += 1    
new_row /= j
print (new_row)

# 3. Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
message = 'asdxfghyxyx'
new_message = ''
VOWELS = 'x'
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
    elif letter.lower() in VOWELS:
        new_message += 'y'
        #print ('Создана новая строка: ', new_message)
print ('\nВот ваш текст: ', new_message)

# 4. Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], кратных и 3 и 5.
row = [3, 4, 56, 100, 15, 2, 20, 30]
new_row: int = 1
index = 0
for i in row:
    if row[index] % 3 == 0 and row[index] % 5 == 0:
        new_row *= row[index]       
    index += 1
print (new_row)

# 5. Заменить все буквы "х" на "у" в исходной строке без использования дополнительной строки.
new_message = ''
VOWELS = 'x'
for letter in 'asdxfghyxyx':
    if letter.lower() not in VOWELS:
        new_message += letter
    elif letter.lower() in VOWELS:
        new_message += 'y'
print ('\nВот ваш текст: ', new_message)
