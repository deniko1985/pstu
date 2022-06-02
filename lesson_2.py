# Описать словарем, списком и множеством предметную область на выбор:
# - автомобили
# - фильмы
# - персонажи игры/книги
# Оценить удобство каждого способа. Объяснить, почему в конкретном случае удобнее тот или иной.
#
# Реализовать поиск элемента.

def list():
    #Премущества списка: не обязательно хэшируемые элементы, упородячен, но допускает повторы, которые сложно отследить при больших объемах данных. 
    characters_list = ['Тирион Ланнистер', 'Серсея Ланнистер', 'Джейме Ланнистер', 'Тайвин Ланнистер', 'Кейтилин Старк', 'Робб Старк', 'Эддард Старк', 'Санса Старк', 'Арья Старк', 'Брандон Старк']
    x_characters_list = input('Введите имя персонажа из сериала "Игра престолов": ')
    if x_characters_list.title() in characters_list:
        print('Этот персонаж существует!')
    else:
        print('Такого персонажа не существует!')
    y_characters_list = int(input('Введите номер индекса персонажа из сериала "Игра престолов": '))
    if characters_list[y_characters_list]:
        print('Вот имя данного персонажа:', characters_list[y_characters_list])
    else:
        print('Такого персонажа не существует!')

def set():
    #Премущества множества: обязательно хэшируемые элементы, неупородячен, не допускает повторы, элементы должны быть уникальны. 
    characters_set = {'Тирион Ланнистер', 'Серсея Ланнистер', 'Джейме Ланнистер', 'Тайвин Ланнистер', 'Кейтилин Старк', 'Робб Старк', 'Эддард Старк', 'Санса Старк', 'Арья Старк', 'Брандон Старк'}
    x_characters_set = input('Введите имя персонажа из сериала "Игра престолов": ')
    if x_characters_set.title() in characters_set:
        print('Этот персонаж существует!')
    else:
        print('Такого персонажа не существует!')

def dict():
    #Премущества словаря: неупородячен, не допускает повторы, т.к. ключи должны быть уникальны. 
    characters_dict = {'Тирион Ланнистер' : 'Дом Ланнистеров', 
                   'Серсея Ланнистер' : 'Дом Ланнистеров', 
                   'Джейме Ланнистер' : 'Дом Ланнистеров', 
                   'Тайвин Ланнистер' : 'Дом Ланнистеров', 
                   'Кейтилин Старк' : 'Дом Старков', 
                   'Робб Старк' : 'Дом Старков',
                   'Эддард Старк' : 'Дом Старков',
                   'Санса Старк' : 'Дом Старков',
                   'Арья Старк' : 'Дом Старков',
                   'Брандон Старк' : 'Дом Старков'}
    x_characters_dict = input('Введите имя персонажа из сериала "Игра престолов": ')
    if x_characters_dict.title() in characters_dict:
        print('Этот персонаж существует! Вот к какому дому он относится:', characters_dict[x_characters_dict])
    else:
        print('Такого персонажа не существует!')

def main():
    print('''
        Где хотите выполнить поиск:
        1 - Поиск по списку
        2 - Поиск по множеству
        3 - Поиск по словарю
        4 - Выход
    ''')
    choise = int(input('Введите выбор: '))
    if choise == 1:
        list()
    elif choise == 2:
        set()
    elif choise == 3:
        dict()
    elif choise == 4:
        print('До свидания.')
    else:
        print('Такого пункта нет.')

main()
