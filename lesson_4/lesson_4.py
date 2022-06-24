from lesson_4_1 import CompareFactory
import pprint

def main():
    new_name_list = []  
    word_list = ['компьютер', 'компьютеризация', 'роза', 'море', 'горе', 'гора', 'персона', 'персонализация', 'терраса', 'территория', 'поза', 'лоза', 'компьютерщик', 'персональность', 'индивидуальность']
    print ('''
    Методы сравнения строк:
    1 - Метод по количеству вхождений одной строки в другую
    2 - Метод Джаро-Винклера
    3 - С применение библиотеки FuzzyWuzzy
    4 - Вычисление растояния Левенштейна
    ''')
    user_input = int(input ('Выберите метод сравнения строк: '))
    while user_input < 1 or user_input > 4:
        user_input = int(input ('Введите правильное значение от 1 до 4: '))
    comparer = CompareFactory.create(user_input)
    for i in word_list:
        for j in word_list:
            if i != j:
                new_name_list.append(comparer.compare(i, j))  
    pprint.pprint(new_name_list)

main()
