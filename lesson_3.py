# Написать модуль, который реализует сравнение строк одним из рассмотренных в лекции методом.
# Написать в модуле конструкцию:
# if __name__ == '__main__'
# в котором провести проверку работы модуля, например как в лекции - парами строк.
#    
# Написать программу, которая перебирает все элементы списка (задан в программе) с некоторой строковой константой (также задана).
#
#
# Данное задание решел немного усложнить и взять не готовый список слов, а текст. После чего текст, преобразуется список со списками пар слов, после чего данные списки
# перебираются, сравниваются и выдает результат сопадений.
import pprint

from lesson_3_1 import words

def main():
    name_text = '''Python является мультипарадигмальным языком программирования, поддерживающим императивное, процедурное, структурное, 
    объектно-ориентированное программирование,
    метапрограммирование и функциональное программирование. Задачи обобщённого программирования решаются за счёт динамической типизации. 
    Аспектно-ориентированное программирование частично поддерживается через декораторы, более полноценная поддержка обеспечивается дополнительными 
    фреймворками.
    Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений. 
    Основные архитектурные черты — динамическая типизация, 
    автоматическое управление памятью, полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной
    блокировкой интерпретатора (GIL),
    высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, 
    могут объединяться в пакеты. (абзац взят из Википедии) передо чрез''' #
    print ('Шаблон текста, который изначально установлен:', name_text)
    user_input = input('\nВведите новый текст, как шаблон или нажмите "Enter", чтобы пропустить:')
    if user_input != '':
        name_text = user_input
        print('\nВы установили новый текст: ', name_text)
    name_text = name_text.lower() # текст приведен к одному регистру. 
    name_list = words(name_text)
    pprint.pprint(name_list)

main()
