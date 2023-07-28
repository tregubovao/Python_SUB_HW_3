# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]
import os
os.system('cls')

my_list = [1, 2, 3, 1, 2, 4, 5]
new_list = []

for el in my_list:
    if my_list.count(el) > 1:
        new_list.append(el)
print(list(set(new_list)))
