# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input("Введите трёхзначное число: "))

c = num % 10
num = num // 10
b = num % 10
a = num // 10

print(f"Сумма цифр трёхзначного числа равна {a + b + c}")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input("Введите общее колличество журавликов: "))

# petya = s // 6
# sergey = petya
# katya = (sergey + petya) * 2

# print(f"Петя сделал {petya}, Серёжа сделал {sergey}, Катя сделала {katya}")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# num = input("Введите шестизначный номер билета: ")
# sum1 = int(num[0]) + int(num[1]) + int(num[2])
# sum2 = int(num[3]) + int(num[4]) + int(num[5])
# if sum1 == sum2:
#     print("Билет счастливый!")
# else:
#     print("Билет обычный :(")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на 
# два прямоугольника). 

# n = int(input("Введите размер стороны шоколадки n: "))
# m = int(input("Введите размер стороны шоколадки m: "))
# k = int(input("Введите колличество долек k: "))

# if(k < m*n) and (k % m == 0 or k % n == 0):
#     print("Можно")
# else:
#     print("Нельзя")
