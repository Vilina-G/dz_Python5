# Задача 1: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def stepen(a, b):
    if b == 1:
        return a
    else:
        return a * stepen(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(f'Число {a} в степени {b} равено: {stepen(a, b)}')

# Задача 2: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# def summ(a , b):
#     if b == 0 :
#         return a
#     else:
#         return summ(a + 1, b - 1)
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(f'Сумма чисел {a} и {b} равена: {summ(a, b)}')
