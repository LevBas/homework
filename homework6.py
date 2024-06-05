# пункт 2 (работа со словарями)
my_dict = {'Alexander': 1990, 'Svetlana': 1985, 'Egor': 1956}
print(my_dict)
print(my_dict['Svetlana'])
print(my_dict.get('Alexey'))
my_dict.update({'Alex': 1965,
                'Sergey': 1998})
a = my_dict.pop('Svetlana')
print(a)
print(my_dict)

# пункт 3 (работа с множествами)
my_set = {1, 2, 3, 'Red', False, (212, 43, 56), 2, 3, 1, 1, 2, 3, 'Red', 'Green'}
print(my_set)
my_set.add(5)
my_set.add('Словарь')
my_set.discard(1)
print(my_set)