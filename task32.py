from random import randint as r

print(lst := [r(1,10) for _ in range(10)])
min_value = int(input('задайте минимальное значение диапазона: '))
max_value = int(input('задайте максимальное значение диапазона: '))

print(ind := [i for i in range(len(lst)) if min <= lst[i] <= max])