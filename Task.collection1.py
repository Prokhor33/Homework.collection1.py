# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

import random

lst = [random.randint(20, 100) for _ in range(100)]
print(lst)

new_list = []
for item in set(lst):
    if lst.count(item) != 1:
        new_list.append(item)
print(new_list)