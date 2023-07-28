# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
import copy
import os
os.system('cls')
my_dict = dict(Вася=("нож", "топор", "спининг", "дошик", "фонарик", "казан"), # нет мангала
                Коля=("нож", "спички", "мангал", "дошик"), # нет топора, казана
                Петя=("мангал", "плащ", "топор", "дошик", "казан"), # ножа
                )
items = []                  # список множеств
names_list = []
for key, value in my_dict.items():
    items.append(set(value))
    names_list.append(key)

uniq_set = items[0] & items[1]
MINLIMIT = 2
for ind in range(MINLIMIT, len(items)):
    uniq_set &= items[ind]
print(f'Все друзья взяли: {(uniq_set)}')

for key, value in my_dict.items():
    res = set(value)
    for name in names_list:        
        if name != key:
            res = res - set(my_dict.get(name))
    print(f'Только {key} имеет: {res}')

for key, value in my_dict.items():
    items2 = copy.deepcopy(items)
    for name in names_list:                               
        if name == key:
            items2.remove(set(value))
    res = items2[0]
    MIN_LIMIT = 1
    for ind in range(MIN_LIMIT, len(items2)):
        res &= items2[ind]
    res_set_absense = res - set(value)
    print(f'Только {key} не имеет: {res_set_absense}')    
