# пункт 2
immutable_var = (1, 2, 3, 'красный', True, [1, 2, 3, 4, 5])
print(immutable_var)

# пункт 3
# immutable_var[5][0] = 3 - в данном случае операция изменения сработает корректно, т.к. изменение идет внутри списка (list), расположенного внутри кортежа
#immutable_var[0] = 2 - в данном случае мы получим ошибку, т.к. пытаемся изменить число (int) внутри кортежа. Аналогичную ошибку получим и при попытки изменения строки (str) и логического типа данных (bool)

# пункт 4
mutable_list = [1, 2, 3]
mutable_list[0] = 'один'
mutable_list[2] = True
print(mutable_list)