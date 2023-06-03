# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exp(b):
    if b==0:
        return 1
    return pow(a,b)

a=int(input('Введите первое число: '))
b=int(input('Введите первое число: '))
print(exp(b))

# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
# 4

def sum_(a,b):
    if (b or a) < 0:
        return False
    return sum_(a+1,b-1)

a=int(input('Введите первое число: '))
b=int(input('Введите первое число: '))
print(sum_(a,b))
