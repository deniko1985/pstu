import re

from pymorphy2 import MorphAnalyzer

def words(name_text):
    ma = MorphAnalyzer()
    new_name_list_1 = []
    new_name_list_2 = []
    preposition = ['без', 'безо', 'близ', 'в', 'во', 'вместо', 'вне', 'для', 'до', 'за', 'из', 'изо', 'из-за', 'из-под', 
                   'к', 'ко', 'кроме', 'между', 'меж', 'на',
                   'над', 'о', 'об', 'обо', 'от', 'ото', 'перед', 'передо', 'пред', 'пред', 'пo', 'под', 
                   'подо', 'при', 'про', 'ради', 'с', 'со', 'сквозь', 'среди', 'у', 'через', 'чрез']
    name_list = re.findall(r'\b(?:[А-Яа-я]{2,})\w+', name_text) # данное регулярное выражение берет из текста только русские слова и исключает союзы, знаки препинания, числа/цифры.
    # данный цикл перебирает списки и удаляет предлоги из основного списка.
    for i in preposition:
        for j in name_list:
            if i == j:
                name_list.remove(j)

    # цикл перебора списка и формирования нового списка, состоящего из списков пар слов
    for i in name_list:
        for j in name_list:
            if i != j:
                nf_i = ma.parse(i)[0].normal_form
                nf_j = ma.parse(j)[0].normal_form
                count = compare (nf_i, nf_j)
                # в итоговый список добавляются только те, пары слов, когда совпадение больше или равно 0.4
                if count >= 0.4:
                    new_name_list_1 = [i, j, nf_i, nf_j, count]
                    new_name_list_2.append(new_name_list_1)

    return new_name_list_2

def compare (S1, S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))] # В переменной создается ссылка на список со срезами входного слова
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram) 
    
    return count / max(len(S1), len(S2))

if __name__ == '__main__':
    print ('Данный модуль работает!')
