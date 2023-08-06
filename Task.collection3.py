things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 'брюки': 1000, 'бумага': 200, 'молоток': 600,
          'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
d = {key: value for key, value in sorted(things.items(),
key=lambda x: x[1], reverse=True)}
my_lst = []
weight = int(input()) * 1000
summa = 0
for key, value in d.items():
    if summa + value <= weight:        my_lst.append(key)
    summa += value
    continue

print(*my_lst)
