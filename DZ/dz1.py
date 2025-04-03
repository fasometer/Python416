# a = 130
# b = 3
# print("a:", a)
# print("b:", b)
# # c = a
# # a = b
# # b = c
# #variant 3
# # a = a + b
# # b = a - b
# # a = a - b
# 2 variant Pyton
# a, b = b, a
# print("a:", a)
# print("b:", b)

# num = int(input("Введите число 5-ти значное число: "))
# print("Ваше число: ",num)
# a = num % 10 # получение первого числа с конца
# num = num // 10 # уменьшение числа на один порядок с конца
# b = num % 10 # получение первого числа с конца
# num = num // 10 # уменьшение числа на один порядок с конца
# c = num % 10 # получение первого числа с конца
# num = num // 10 # уменьшение числа на один порядок с конца
# d = num % 10 # получение первого числа с конца
# num = num // 10 # уменьшение числа на один порядок с конца
# f = num % 10 # получение первого числа с конца
# print("В него входят числа: ", f, d, c, b, a() # вывод чисел
# print("Произведение чисел: ", a * b * c * d * f() # вывод чисел
# print("Среднее арифметическое: ", (a + b + c + d + f) / 5) # вывод чисел

# n = int(input("Введите число от 1 до 99: "))
# kop = n
# kop = kop % 10 # для ускорения работы программы
# if 1 <= n <= 99:
#     if 11 <= n <= 14:
#         print(n, "копеек")
#     elif kop == 1:  # and n != 11
#         print(n, "копейка")
#     elif 2 <= kop <= 4:  # and n != 12 and n != 13 and n != 14
#         print(n, "копейки")
#     else:
#         print(n, "копеек")
# else:
#     print("Число вне диапазона")

# n = input("Укажите количество символов: ")
# while True:
#     while type(n) is not int:
#         try:
#             n = int(n)
#         except ValueError:
#             print("Число не целое")
#             n = input("Укажите количество символов: ")
#
#     while int(n) <= 0:
#         print("Число должно быть больше 0")
#         n = input("Укажите количество символов: ")
#     if int(n) > 0:
#         break
#
# n = int(n)
# sim = input("Введите символ: ")
# t = input("0 - горизонтальное направление \n1- вертикальное направление\nВаш выбор: ")
# while type(t) is not int:
#     try:
#         t = int(t)
#     except ValueError:
#         print("Это не число")
#         t = input("Укажите Ваш выбор числом 0 или 1: ")
#
# if 0 <= int(t) <= 1:
#     t = int(t)
# else:
#     t = input("Укажите Ваш выбор числом 0 или 1: ")
#
# t = int(t)
# if t == 0:
#     while n > 0:
#         print(sim, end=" ")
#         n -= 1
# else:
#     while n > 0:
#         print(sim)
#         n -= 1


# a = [int(input("-> ")) for i in range(int(input("n = ")))]  # генератор списка
# res = 0
# for _ in range(len(a)):
#     if a[_] < 0:
#         res += a[_]
# print("Сумма отрицательных элементов:", res)
# вариант питона код короче
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = 0
# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов: ", s)


# вывод элементов встречающихся один раз два варианта
# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# new_lst = []
# i = 0
# for element in lst:
#     k = element
#     for j in lst:
#         if k == j:
#             i += 1
#     if i == 1:
#         print(k, end=" ")
#         new_lst.append(k)
#     i = 0
# print()
# print("Первый вариант: ")
# print(new_lst)
#
# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# new_lst = []
# for element in lst:
#     if lst.count(element) == 1:
#         new_lst.append(element)
# print("Второй вариант: ")
# print(new_lst)


# import random
#
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print("Первый вариант")
# new_mas = sorted(mas.copy())
# new1_mas = mas.copy()
# print("Min value:", new_mas[0])
# index = mas.index(new_mas[0])
# print("Min index:", mas.index(new_mas[0]))
# del mas[:index]
# print(mas)
# print("Второй вариант")
# print("Min value", min(new1_mas))
# ind = new1_mas.index(min(new1_mas))
# print("Index min", ind)
# new1_mas[:ind] = []
# print(new1_mas)

# from math import pi, sqrt
#
# print("Вычисление площади фигур\n\nВыбор фигуры:\n 1 - треугольник\n 2 - прямоугольник\n 3 - круг")
# vb = input("Ваш выбор: ")
# s = None
# match vb:
#     case "1":
#         print("Расчет треугольника:"
#         a = int(input("Введите сторону а = "))
#         b = int(input("Введите сторону b = "))
#         c = int(input("Введите сторону c = "))
#         p = (a + b + c) / 2
#         if (p - a) * (p - b) * (p - c) > 0:
#             s = sqrt(p * (p - a) * (p - b) * (p - c))
#             print("Его площадь", round(s, 2))
#         elif p - b <= 0:
#             print("Сторона b не подходит")
#         elif p - c <= 0:
#             print("Сторона c не подходит")
#         elif p - a <= 0:
#             print("Сторона a не подходит")
#     case "2":
#         print("Расчет прямоугольника:"
#         a = int(input("Введите длину = "))
#         b = int(input("Введите ширину = "))
#         s = a * b
#         print("Его площадь", round(s, 2))
#     case "3":
#         print("Расчет круга:")
#         a = int(input("Введите радиус круга = "))
#         s = pi * a ** 2
#         print("Его площадь", round(s, 2))
#     case _:
#         print("Неверный выбор")

# def symbol_in_rad(quantity=20, sim="-"):
#     print(sim*quantity)
#     print()
#
#
# symbol_in_rad()
# symbol_in_rad(10, "+")
# symbol_in_rad(5, "*")
# symbol_in_rad(sim="#")
# symbol_in_rad(5)
# symbol_in_rad()
# symbol_in_rad(7, "kol")


#   print(tuple(input("->") for i in range(5)))  # генератор кортежа
#   print(tuple(randint(0, 5) for i in range(10)))

# from random import randint
#
#
# def func(first, last):
#     return tuple(randint(first, last) for _ in range(10))
#
#
# tpl1 = func(0, 5)
# tpl2 = func(-5, 0)
# tpl_new = tpl1 + tpl2
# print(tpl1)
# print(tpl2)
# print(tpl_new)
# print("Кол-во 0 =", tpl_new.count(0))

# st1 = "Python"
# st2 = "Programming language"
# print("Первая строка:", st1)
# print("Вторая строка:", st2)
# print("Искомые буквы")
# for _ in set(st1) - set(st2):
#     print(_, end=" ")

# dict_sales = {
#     "John": {
#         "N": 3056,
#         "S": 8463,
#         "E": 8441,
#         "W": 2694
#     },
#     "Tom": {
#         "N": 4832,
#         "S": 6786,
#         "E": 4773,
#         "W": 3612
#     },
#     "Anne": {
#         "N": 5239,
#         "S": 4802,
#         "E": 5820,
#         "W": 1859
#     },
#     "Fiona": {
#         "N": 3904,
#         "S": 3645,
#         "E": 8821,
#         "W": 2451
#     }
# }
# for x, y in dict_sales.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ":", j)
# name = input("Введите имя: ")
# region = input("Введите регион: ")
#
# while True:
#     try:
#         dict_sales[name][region] = int(input("Новое значение: "))
#         break
#     except ValueError:
#         print("Значение не корректно. Введите число")
# print(name, dict_sales[name])


# Первый вариант
# kol = int(input("Количество студентов: "))
# name, ball = [], []
# for i in range(1, kol + 1):
#     print(i, end="")
#     name.append(input("-й студент: "))
#     ball.append(int(input("Балл: ")))
# student = dict(zip(name, ball))
# print()
# average = round(sum(ball) / kol)
# print("Средний балл: ", average, ". Студенты с баллом выше среднего:", sep="")
# for k, v in student.items():
#     if v > average:
#         print(k)

# Второй вариант
# kol = int(input("Количество студентов: "))
# student = {}
# res = 0
# for i in range(kol):
#     name = input(str(i + 1) + "-й студент: ")
#     ball = int(input("Балл: "))
#     res += ball
#     student[name] = ball
# print()
# average = round(res / kol)
# print("Средний балл: ", average, ". Студенты с баллом выше среднего:", sep="")
# for k, v in student.items():
#     if v > average:
#         print(k)

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(8, 6, 1))
#
# s1 = 1
#
#
# def outer1(a, b, c):
#     global s1
#
#     def inner(i, j):
#         return i * j
#
#     s1 = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# outer1(2, 4, 6)
# print(s1)
# outer1(5, 8, 2)
# print(s1)
# outer1(8, 6, 1)
# print(s1)
#
#
# def outer2(a, b, c):
#     def inner():
#         nonlocal a, b, c
#         return a * b + a * c + c * b
#
#     s = 2 * inner()
#     return s
#
#
# print(outer2(2, 4, 6))
# print(outer2(5, 8, 2))
# print(outer2(8, 6, 1))
#
#
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner  # возвращает вложенную функцию
#
#
# func1 = outer(5)
# print(func1(10))
#
# func2 = outer(6)
# print(func2(16))

# from math import pi
#
# area = {
#     "Круг": lambda x: pi * x ** 2,
#     "Прямоугольник": lambda a, b: a * b,
#     "Трапеция": lambda a, b, h: (a + b) * h / 2,
# }
# r, a2, b2, a1, b1, h1 = 2, 10, 13, 7, 5, 3
# print("Площадь окружности радиуса ", r, ": ", area["Круг"](r), sep="")
# print("Площадь прямоугольника размером ", a2, "*", b2, ": ", area["Прямоугольник"](a2, b2), sep="")
# print("Площадь трапеции a=", a1, " ,b=", b1, " ,h=", h1, ": ", area["Трапеция"](a1, b1, h1), sep="")

# def average(fn):
#     def inner(args):
#         st = ""
#         for i in args:
#             st += str(i) + ", "  #sr[:-2]
#         return fn(args) / len(args)
#
#     return inner
#
#
# def sum_num(num):
#     return sum(num)
#
#
# g = (2, 3, 3, 4)
# print("Сумма чисел", *g, "=", sum_num(g))
#
#
# @average
# def sum_num(num):
#     return sum(num)
#
#
# print("Среднее арифметическое чисел", *g, "=", sum_num(g))

# st = "I am learning Python. hello, WORLD!"
# first = st.index("h")
# second = st.index("h", first + 1)
# s = st[first:second]
# print(st)
# print(st[:st.find("h")] + s[::-1] + st[second + 1:])

# import re
#
# st = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg = r"[\w\-\_\d\.]+@[\w\.]+"
# print(re.findall(reg, st))

# print("ДЗ через репозиторий")
# num = [5, -5, 5, -5, -5, 5, 5, -5]
#
#
# def sum_neg(lst):
#     res = 0
#     if len(lst) == 0:
#         return 0
#     else:
#         # print(lst, "=> lst[0]:", lst[0])
#         if lst[0] < 0:
#             res = 1
#         else:
#             res = 0
#     return res + sum_neg(lst[1:])
#
#
# print(num)
# print("Всего отрицательных чисел в списке:", sum_neg(num))

# file = "zamena.txt"
# test = "Замена строки в текстовом файле:\nизменить строку в списке;\nзаписать список в файл;\n444\n555\n6666\n"
# f = open(file, "w")
# f.write(test)
# f.close()
# with open(file) as f:
#     print(f.read())
# with open(file) as f:
#     read_line = f.readlines()   # получили список
#     print("В файле строк: ", len(read_line))
#
# pos1 = int(input("Введите номер исходной строки: "))
# while True:
#     if 0 <= pos1 <= len(read_line):
#         break
#     else:
#         pos1 = int(input("Такой строки нет \nВведите номер исходной строки: "))
# pos2 = int(input("Номер строки для замены: "))
# while True:
#     if 0 <= pos2 <= len(read_line):
#         break
#     else:
#         pos2 = int(input("Такой строки нет \nНомер строки для замены: "))
#
# read_line[pos1 - 1], read_line[pos2 - 1] = read_line[pos2 - 1], read_line[pos1 - 1]
#
# with open(file, "w") as f:
#     f.writelines(read_line)
#
# with open(file) as f:
#     print(f.read())

# import os
# import time
#
# file = input("Введите путь :")
# print(file)
# # file = r"test\f1\new.txt"
# if os.path.exists(file):  # ПРОВЕРКА наличия пути
#     tpl = os.path.split(file)  # два кортежа
#     s = os.path.getatime(file)
#     print(tpl[1], " (", tpl[0], ") "," - ", "last access ",
#           time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(s)), sep="")
# else:
#     print("Файла нет")

class Car:
    def __init__(self, model=1, yars=1, manufacter=1, power=2, color=2, price=2):
        self.__yars = yars
        self.__model = model
        self.__manufacter = manufacter
        self.__power = power
        self.__color = color
        self.__price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.__model}\nГод выпуска: {self.__yars}\n"
              f"Производитель: {self.__manufacter}\nМощность двигателя: {self.__power} л.с.\n"
              f"Цвет машины: {self.__color}\nЦена: {self.__price}")
        print("=" * 40)


p1 = Car(3,3,3,3,3,3)
p1.print_info()
