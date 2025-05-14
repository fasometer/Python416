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
# test = "Замена строки в текстовом файле:\n изменить строку в списке;\n записать список в файл;\n444\n555\n6666\n"
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
#     t = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(s))
#     print(f"{tpl[1]} ({tpl[0]}) - last access {t}")
#     # print(tpl[1], " (", , ") ", " - ", "", t, sep="")
# else:
#     print("Файла нет")
# import datetime
#
#
# class Car:
#     def __init__(self, model, yars, manufacturer, power, color, price):
#         self.__yars = yars
#         self.__model = model
#         self.__manufacturer = manufacturer
#         self.__power = power
#         self.__color = color
#         self.__price = price
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.__model}\nГод выпуска: {self.__yars}\n"
#               f"Производитель: {self.__manufacturer}\nМощность двигателя: {self.__power} л.с.\n"
#               f"Цвет машины: {self.__color}\nЦена: {self.__price} rub")
#         print("=" * 40)
#
#     def set_model(self, model):
#         if isinstance(model, str):
#             self.__model = model
#         else:
#             print("Должен быть текст")
#
#     def set_yars(self, yars):
#         today = datetime.date.today()
#         if isinstance(yars, int) and 1900 <= yars <= today.year:
#             self.__yars = yars
#         else:
#             print("Год не похож на себя")
#
#     def set_manufacturer(self, manufacturer):
#         if isinstance(manufacturer, str):
#             self.__manufacturer = manufacturer
#         else:
#             print("Должен быть текст")
#
#     def set_power(self, power):
#         if isinstance(power, int) and 10 <= power <= 2000:
#             self.__power = power
#         else:
#             print("Мощность не корректна")
#
#     def set_color(self, color):
#         if isinstance(color, str):
#             self.__color = color
#         else:
#             print("Должен быть текст")
#
#     def set_price(self, price):
#         if isinstance(price, int) and 0 <= price:
#             self.__price = price
#         else:
#             print("Цена не корректна")
#
#     def get_model(self):
#         return self.__model
#
#     def get_yars(self):
#         return self.__yars
#
#     def get_manufacturer(self):
#         return self.__manufacturer
#
#     def get_power(self):
#         return self.__power
#
#     def get_color(self):
#         return self.__color
#
#     def get_price(self):
#         return self.__price
#
#
# p1 = Car("X7 M50i", 2021, "BMW", 530, "white", 1079000)
# p1.print_info()
# p1.set_model("X56 OPO")
# print(p1.get_model())
# p1.set_yars(2026)
# print(p1.get_yars())
# p1.set_manufacturer("BMW")
# print(p1.get_manufacturer())
# p1.set_power(30000)
# print(p1.get_power())
# p1.set_color("black")
# print(p1.get_color())
# p1.set_price(-30000)
# print(p1.get_price())
# p1.print_info()
# import math
#
#
# class Sqwer:
#     __count = 0
#
#     @staticmethod
#     def sq_triangle_geron(a, b, c):
#         p = (a + b + c) / 2
#         Sqwer.__count += 1
#         return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
#
#     @staticmethod
#     def sq_triangle_visota(a, h):
#         Sqwer.__count += 1
#         return a * h / 2
#
#     @staticmethod
#     def sq_rectangle(a, b):
#         Sqwer.__count += 1
#         return a * b
#
#     @staticmethod
#     def sq_square(a):
#         Sqwer.__count += 1
#         return a ** 2
#
#     @staticmethod
#     def get_count():
#         return Sqwer.__count
#
#
# print("Площадь вычислялась:", Sqwer.get_count())
# print("Площадь треугольника:", Sqwer.sq_triangle_geron(3, 4, 5))
# print("Площадь треугольника:", Sqwer.sq_triangle_geron(5, 6, 7))
# print("Площадь вычислялась:", Sqwer.get_count())
# print("Площадь треугольника:", Sqwer.sq_triangle_visota(5, 6))
# print("Площадь прямоугольника:", Sqwer.sq_rectangle(6, 7))
# print("Площадь квадрата:", Sqwer.sq_square(6))
# print("Площадь квадрата:", Sqwer.sq_square(7))
# print("Площадь квадрата:", Sqwer.sq_square(8))
# print("Площадь вычислялась:", Sqwer.get_count())

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет №{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):  # магические методы
#         print("*" * 50)
#         print(f"Счет №{self.__num} принадлежащий {self.__surname} был закрыт.")
#
#     @staticmethod  # переврд в доллары или евро статические
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):  # изменение статического метода методом класса
#         cls.rate_eur = rate
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, n):
#         self.__num = n
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, n):
#         self.__surname = n
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, n):
#         self.__percent = n
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, n):
#         self.__value = n
#
#     def confert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_euro(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_precents(self):
#         self.__value += self.__value * self.__percent
#         print("проценты были начислены")
#         self.print_balans()
#
#     def withdraw_money(self, val):
#         if val >= self.__value:
#             print(f"Нет суммы {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было снято")
#         self.print_balans()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было добавлено")
#         self.print_balans()
#
#     def print_balans(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"# {self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balans()
#         print(f"Проценты: {self.__percent:.0%}")  # расчет процента с точностью до ,0 за счет f строки
#         print("-" * 20)
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_info()
# # acc.__del__()
# print()
# acc.value = 5000
# acc.surname = "Петров"
# acc.num = 987654
# acc.percent = 0.05
# acc.print_info()
# # acc.__del__()
# print()
#
#
# class Account_1:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет №{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):  # магические методы
#         print("*" * 50)
#         print(f"Счет №{self.__num} принадлежащий {self.__surname} был закрыт.")
#
#     @staticmethod  # переврд в доллары или евро статические
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):  # изменение статического метода методом класса
#         cls.rate_eur = rate
#
#     def get_num(self):
#         return self.__num
#
#     def set_num(self, n):
#         self.__num = n
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_surname(self, n):
#         self.__surname = n
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_percent(self, n):
#         self.__percent = n
#
#     def get_value(self):
#         return self.__value
#
#     def set_value(self, n):
#         self.__value = n
#
#     def confert_to_usd(self):
#         usd_val = Account_1.convert(self.__value, Account_1.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account_1.suffix_usd}")
#
#     def convert_to_euro(self):
#         eur_val = Account_1.convert(self.__value, Account_1.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account_1.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_precents(self):
#         self.__value += self.__value * self.__percent
#         print("проценты были начислены")
#         self.print_balans()
#
#     def withdraw_money(self, val):
#         if val >= self.__value:
#             print(f"Нет суммы {val} {Account_1.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account_1.suffix} было снято")
#         self.print_balans()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account_1.suffix} было добавлено")
#         self.print_balans()
#
#     def print_balans(self):
#         print(f"Текущий баланс {self.__value} {Account_1.suffix}")
#
#     def print_info(self):
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"# {self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balans()
#         print(f"Проценты: {self.__percent:.0%}")  # расчет процента с точностью до ,0 за счет f строки
#         print("-" * 20)
#
#
# acc1 = Account_1("123450", "Дол", 0.02, 100)
# acc1.print_info()
# acc1.set_value(15000)
# acc1.set_surname("Петровa")
# acc1.set_num(9876540)
# acc1.set_percent(0.15)
# acc1.print_info()

# class Rect:
#     def __init__(self, wight, height):
#         self.width = wight
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник: \nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, wight, height, background):
#         super().__init__(wight, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()  # доступ к родительскому классу
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, wight, height, wight_border, type_border, color_border):
#         super().__init__(wight, height)  # доступ к init родительского класса
#         self.wight = wight_border
#         self.type = type_border
#         self.color = color_border
#
#     def show_rect(self):
#         super().show_rect()  # доступ к методу родительского класса
#         print(f"Ширина рамки: {self.wight}\nТип рамки: {self.type}\nЦвет рамки: {self.color}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 400, "1px", "solid", "blue")
# shape2.show_rect()

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.nout = self.Nout()
#
#     def show(self):
#         return self.name
#
#     class Nout:
#         def __init__(self):
#             self.name = "HP"
#             self.cpu = "i7"
#             self.ram = "16"
#
#         def show(self):
#             return self.name, self.cpu, self.ram
#
#         # def show(self):
#         #     return print(f"{self.name}, {self.cpu}, {self.ram}")
#
#
# st = Student("Roman")
# n = st.nout
# print(f"{st.show()} => ",end="")
# print(*n.show(), sep=" ,")
# st1 = Student("Vladimir")
# n1 = st.nout
# print(f"{st1.show()} => ", (', '.join(n1.show())))

# число секунд в дне 24* 60 * 60 = 86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("секунды число!!")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):  # сумма
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):  # разность
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):  # умножение
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):  # деление
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):  # остаток от деления
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):    # равно
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):    # не равно
#         return not self.__eq__(other)
#
#     def __lt__(self, other):    # меньше
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return self.sec < other.sec
#
#     def __gt__(self, other):    # больше
#         return not self.__lt__(other)
#
#     def __le__(self, other):    # меньше или равно
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return self.sec <= other.sec
#
#     def __ge__(self, other):    # больше или равно
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый тоже должен быть тип Clock")
#         return self.sec >= other.sec
#
#
# c1 = Clock(6)
# c2 = Clock(2)
# print("c1:", c1.get_format_time())
# print("c2:", c2.get_format_time())
# print("c1 - c2:", (c1 - c2).get_format_time())
# print("c1 * c2:", (c1 * c2).get_format_time())
# print("c1 // c2:", (c1 // c2).get_format_time())
# print("c1 % c2:", (c1 % c2).get_format_time())
# c1 -= c2
# print("c1 -= c2:", c1.get_format_time())
# c1 = Clock(6)
# c2 = Clock(2)
# print("c1:", c1.get_format_time())
# print("c2:", c2.get_format_time())
# c1 *= c2
# print("c1 *= c2:", c1.get_format_time())
# c1 = Clock(6)
# c2 = Clock(2)
# print("c1:", c1.get_format_time())
# print("c2:", c2.get_format_time())
# c1 //= c2
# print("c1 //= c2:", c1.get_format_time())
# c1 = Clock(6)
# c2 = Clock(5)
# print("c1:", c1.get_format_time())
# print("c2:", c2.get_format_time())
# c1 %= c2
# print("c1 %= c2:", c1.get_format_time())
# c1 = Clock(6)
# c2 = Clock(5)
# print("c1:", c1.get_format_time())
# print("c2:", c2.get_format_time())
# if c1 == c2:
#     print("время равно")
# else:
#     print("Время разное")
#
# if c1 != c2:
#     print("время разное")
# else:
#     print("Время равно")
# if c1 > c2:
#     print("c1 > c2 True")
# else:
#     print("c1 > c2 False")
# if c1 < c2:
#     print("c1 < c2 True")
# else:
#     print("c1 < c2 False")
# c1 = Clock(6)
# c2 = Clock(8)
# if c1 <= c2:
#     print("c1 <= c2 True")
# else:
#     print("c1 <= c2 False")
# if c1 >= c2:

#     print("c1 >= c2 True")
# else:
#     print("c1 >= c2 False")
# from math import sqrt
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def info(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def square(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, w, h, color):
#         super().__init__(color)
#         self.w = w
#         self.h = h
#
#     def info(self):
#         print("===Прямоугольник===")
#         print(f"Длина: {self.w}")
#         print(f"Ширина: {self.h}")
#         print(f"Цвет: {self.color}")
#
#     def perimeter(self):
#         return print(f"Периметр: {2 * (self.w + self.h)}")
#
#     def square(self):
#         return print(f"Площадь: {self.w * self.h}")
#
#     def draw(self):
#         for i in range(self.h):
#             for j in range(self.w):
#                 print("* ", end="")
#             print()
#
#
# class Square(Shape):
#     def __init__(self, a, color):
#         super().__init__(color)
#         self.a = a
#
#     def info(self):
#         print("===Квадрат===")
#         print(f"Сторона: {self.a}")
#         print(f"Цвет: {self.color}")
#
#     def perimeter(self):
#         return print(f"Периметр: {4 * self.a}")
#
#     def square(self):
#         return print(f"Площадь: {self.a ** 2}")
#
#     def draw(self):
#         for i in range(self.a):
#             for j in range(self.a):
#                 print("* ", end="")
#             print()
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c, color):
#         super().__init__(color)
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def info(self):
#         print("===Треугольник===")
#         print(f"Сторона 1: {self.a}")
#         print(f"Сторона 2: {self.b}")
#         print(f"Сторона 3: {self.c}")
#         print(f"Цвет: {self.color}")
#
#     def perimeter(self):
#         return print(f"Периметр: {self.a + self.b + self.c}")
#
#     def square(self):
#         p = (self.a + self.b + self.c) / 2
#         return print(f"Площадь: {round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)}")
#
#     def draw(self):
#         for i in range(1, self.a + 1):
#             print(' ' * self.a + '*' * (i * 2 - 1))
#             self.a -= 1
#
#
# shapes = [
#     Rectangle(7, 3, "green"),
#     Square(3, "red"),
#     Triangle(6, 6, 11, "yellow")
# ]
#
# for i in shapes:
#     i.info()
#     i.perimeter()
#     i.square()
#     i.draw()
#     print()
# from cars import *
#
#
# car_1 = car.Car("Tesla", "T", 2018, 99100)
# print(car_1.info())
# car_2 = elec.Electro("Tesla", "T_2", 2025, 100, 100)
# print(car_2.info())

import json
from random import choice


def gen_person():
    name = ' '
    tel = ' '

    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }
    k = tel
    return person,k


def write_json(person_dict):
    try:
        data = json.load(open("persons.json"))
    except FileNotFoundError:
        data = {}
    k = person_dict[1]
    data[k] = person_dict[0]

    with open("persons.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
print(gen_person())
