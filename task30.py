value = int(input('введите первый элемент: '))
difference = int(input('введите разность: '))
all = int(input('введите количество элементов: '))

print(lst := [i for i in range(value, value+difference*(all-1)+1, difference)])