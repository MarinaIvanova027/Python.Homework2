# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите колличество элементов: "))
for i in range(n):
    print(f'{a1 + i * d}', end=' ')

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
min = int(input("Введите минимум диапазона: "))
max = int(input("Введите максимум диапазона: "))
for i in range(len(list)):
    if min <= list[i] <= max:
        print(i)