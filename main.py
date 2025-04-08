# name = "admin" # переменная типа str
# # print("Hello, " + name + "!")
# age = 20
# print(age)
# agt = 3.2
# age = 15.8
# # print(name + str(age))
# print(type(name))
# print(type(age))
# print(type(agt))
# print(age)
# a = 4
# b = 5
# print(id(a))
# print(id(b))
# a = b
# print(id(a))
# print(id(b))
# a = b = c = 1 # множественное присваивание
# print(a)
# print(b)
# print(c)
# print(id(a))
# a, b, c = 5, "hello", 9.2
# print(a)
# print(b)
# print(c)
# import keyword
# print(keyword.kwlist)
# _first_name = "admin"
# print(_first_name)
# PI = 3.14
# print(PI)
# PI = 6.3
# print(PI)
# name = "Никита"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут " + name + ". Мне" ,age, "лет.")
# print(" строка\
#  символов")
# print(' строка \n символов')
# print("\tДокумент \"file.txt\"   \r   находится по пути c:\\desktop\\folder")
# from pkgutil import walk_packages
# from zope.interface import named
# from setuptools.config import read_configuration
# from itertools import count
# from multiprocessing.spawn import old_main_modules


# a = 5
# b = 7
# c = 3
# res = a + b + c
# print("Сумма",res )
# print("Произведение", a * b * c)
# print("Среднее", res / 3)

# print(6 + 4 * 5 ** 2 + 7)
# print((6 + 4) * (5 ** 2 + 7))

# num = 10
# num += 5
# print(num)
# num -= 3
# print(num)
# num **= 2 #num = num **2

# print(num)
# num = 4321
# print(num)
# a = num % 10
# num = num // 10
# print("a ", a)
# print(num)
# b = num % 10
# print("b ", b)
# num = num // 10
# print(num)
# c = num % 10
# print("c ", c)
# num = num // 10
# print(num)
# d = num % 10
# print("d ", d)
# print("Обратное число ", a, b, c, d)
# print("Обратное число ", a * 1000 + b * 100 + c * 10 + d)

# num = 6543 # перевернуть числа остаток от деления и деление на цело
# print(num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
# res = num1 + str(num2)
# print(res)

# print(int(3.8))
# print(round(3.85))
# print(type(round(3.85)))
# print(round(3.891, 2))
# print(type(round(3.891, 2)))
# print(round(3.899, 2))

# a = '5.2'
# b = 10
# res = float(a) + b
# print(res)

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="",end="\n\n")
# print("Новая строка")

# name = input("Введите имя: ")
# print("Ваше имя: ", name)

# num = int(input("Ввести чисто: "))
# power = int(input("Степень: "))
# # num= int(num)
# # power=int(power)
# res = num ** power
# print("Число", num, "в степени",power ,"результат",res)
#
# num1 = int(input("Ввести первое число: "))
# num2 = int(input("Ввести второе число: "))
# num3 = int(input("Ввести третье число: "))
# num4 = int(input("Ввести четвертое число: "))
# print(round((num1 + num2)/(num3+num4),2))

# b1 = True
# b2 = False
# print(type(b1))
# print(b1 + 5)

# False => "" or 0 or 0.0 or False or None
# print(bool("pyton"))
# print(bool(""))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))
# a = None
# print(a)
# print(type(a))
# print(7 == 7)
# print(2 + 5 == 7 / 3)
# print(2 + 5 != 7 / 3)
# print(8 < 5)
# print(8 >= 8)
# print("pytoN" > "pyTon") # коды ASCII сравнивает слева направо и находит первое отличие

# print(2 < 4 < 9)  # true && True => True
# print(2 * 5 > 7 >= 4 + 3)  # 10>7>=7
# print(3 * 3 <= 7 >= 2)  # 9<=7>=2  False &&True =>False
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # опреатор и
# print(5 - 3 == 2 and 1 + 3 < 4)
# print(5 - 3 == 2 or 1 + 3 == 4)  # оператор или   ! not
# print(5 - 3 == 2 or 1 + 3 < 4)
# print(not 5 - 5)  # not
# print(not 9 - 5)
# a = 5
# print("a:", a)
# print("строка текста строка текстастрока текстастрока текстастрока текстастрока текстастрока текстастрока
# текстастрока "
#       "текстастрока текста")
#
# cnt = 5
# if cnt < 10:  # тогда обоз :
#     cnt = cnt + 1  # 4 пробельных символа или табуляция
#     cnt += 1
#     print(cnt)
# age = int(input("Введите свой возраст: "))  # приведение типов в цифру
# if age >= 18:
#     print("Вход разрешен")
# else:
#     print("Рано еще")
# a = 25
# b = 25
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a = b")
# else:
#     print("b > a")

# a = input("Введите первую сторону: ")
# b = input("Введите второю сторону: ")
# c = input("Введите третью сторону: ")
# if a == b == c:
#     print("Равносторонний треугольник")
# elif a == b or a == c or b == c:
#     print("Равнобедренный треугольник")
# else:
#     print("Разносторонний треугольник")

# day = int(input("введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print(" понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня нет")

# season = int(input("Введите номер месяца: "))
# if 1 <= season <= 12:
#     print("Время года: - ",end-"")
#     if 1 <= season <= 2 or season == 12:
#         print("Зима")
#     if 3 <= season <= 5:
#         print("Весна")
#     if 6 <= season <= 8:
#         print("Лето")
#     if 9 <= season <= 11:
#         print("Осень")
# else:
#     print("Такого месяца нет")

# n = int(input("Введите число ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода")

# match выражение:
#     case шаблон_1:
#         действие_1
#     case _:
#         значение по умолчанию

# passwrd = "admin1"
#
# match passwrd:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("пользователь")
#     case _:  # если ничего не подошло и ставится в конце
#         print("Пароль не верен")
# day = "вторник"
# time = 18
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня нет или нерабочее время")

# тернарное выражение

# a, b = 100, 20
# print(a if a < b else b)


# a, b = 10, 0
# print("На ноль делить нельзя" if b == 0 else a / b) # нельзя присвоить или два действия

# a = 0
# b = 0
# print(a / b)

# try:  # для контроля ввода исключения
#     n = int(input("Ввести целое число "))
#     print(n * 2)
# except ValueError:  # то что проверяют
#     print("Что-то пошло нет так")
# try:
#     n = int(input("введите делимое:  "))
#     m = int(input("введите делитель:  "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else:   # когда не возникли исключения
#     print("Все нормально Вы ввели ", n, "и", m)
# finally:    # выполняется в любом случае может быть один с try
#     print("Конец программы ")


# n = input("Введите первое число:  ")
# m = input("Введите второе число:  ")
# try:
#     # print(int(n) + int(m))
#     n = int(n)
#     m = int(m)
# except ValueError:
#     # print(str(n) + str(m))
#     n = str(n)
# finally:
#     print(n + m)

# циклы
# while условие:
#     блок кода
# итерация один шаг цикла
# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 5:
#     print("i =", i)
#     i -= 1
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
# print()
# j = 2
# while j <= 20:
#     print(j, end=" ")
#     j += 2
# n = int(input("Укажите количисво символов:  "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1
# n = int(input("Укажите количисво символов:  "))
# print("*" * n)

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a
#     a += 1
# print()
# print("Сумма нечетных чисел: ", res)

# n = input("Введите целое число: ")
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue    # исключение из цикла переход на проверку по условию
#     print(i, end=" ")
#     if i == 5:
#         break  # прерываем цикл по условию
#     i += 1
# print("\nЦикл завершен")
# бесконечные циклы
# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")
# ввод какого кол-во чисел
# while True:
#     n = int(input("введите положительное число: "))
#     if n < 0:
#         break
# print("\nЦикл завершен")
# res = 1
# while True:
#     n = int(input("введите  число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i< 10:
#     print(i)
#     i += 1
# else:  # отработает если цикл полностью закончился без прерываний
#     print("Цикл завершен, i= ", i)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:  # отработает если цикл полностью закончился без прерываний
#     print("Цикл завершен, i= ", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\t Внутренний цикл: j =", j)
#         j += 1
#     i += 1
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", j * i, end="\t\t")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(elemen)

# for i in "Hello":
#     print(i)
# for i in "Hello", "World":
#     print(i)

# range(start, stop ,step=1)

# print(range(10)) # можно не писать первывй ноль и последнюю единицу
# for i in range(10, 0, -2):
#     print(i, end=" ")
# print()
# j = 10
# while j > 0:
#     print(j, end=" ")
#     j -= 1
# a = int(input("Введите число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
# print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     if i == 1:
#         continue
#         #break
#     print(i)
# else:  # только если условие не было прервано
#     print("Конец цикла")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("\t------")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
# string = [letter * 2 for letter in "Python"]
# print(string)
#
# for letter in "Python":
#     print(letter * 2, end="\t")

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
# print()
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end=" ")
# Список (list)
# nums = [0, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
#
# num1 = list()
# print(num1)

# nums = [0, 3, 9, 4, 1, "one", True]
# print(nums)
# print(nums[0])
# print(nums[-5])
# print(nums[-1])
# print(nums[-2])

# nums = [8, 3, 9, 4, 1]
# print(nums)
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums, id(nums)) # индекс памяти для списка но не его значения изменяемый тип данных
# print(nums[0], id(nums[0])) # индекс памяти конкретного значения списка
# print(nums[1], id(nums[1])) # индекс памяти конкретного значения списка
# nums[1] = 256
# print(nums[1], id(nums[1]))
# print(nums, id(nums))
# # print(nums[5]) # выходит за индекс списка те исключения
# print("длина списка:", len(nums))

# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 13]
# n = nums + nums2
# print(n)
# print(n * 2)

# print(list("Hello"))
# print(range(10))
# print(list(range(10)))
# print(list(range(10, 2, -2)))

# [выражение for  переменная in последовательность

# a = [0 for _ in range(5)]
# print(a)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [0] * int(input("введите кол-во элементов в списке: "))
# print(a) # создали пустой список
# for i in range(len(a)):
#     a[i] = int(input("-> "))   # заполнение списка числами
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]  # генератор списка
# print(a)

# a = list(range(10, 100, 10))
# print(a)
# for i in range(len(a)):   # 0 1 2 3 4 5 6 7 8
#     # print(i, end=' ')
#     print(a[i], end=" ")   # если нужен индекс для работы
# print()
#
# for i in a:   # может только питон
#     print(i, end=" ")

# a = [int(input("-> ")) for _ in range(int(input("n = ")))]  # генератор списка
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# a = [int(input("-> ")) for _ in range(int(input("n = ")))]
# for i in a:
#     if i < 0:
#         s += i
# i = 0
# while i < len(a):
#     if a[i] < 0:
#         s += a[i]
#     i += 1
# print("Сумма отрицательных элементов: ", s)

# a = [int(input("-> ")) for _ in range(int(input("n = ")))]
# s = 0
# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов: ", s)

# a = [int(input("-> ")) for _ in range(int(input("n = ")))]
# print(a)
#
# for i in range(len(a)):
#     if i % 2 == 0:   # считаем четный индекс
#         print(a[i], end=" ")
# print()
# for i in range(0, len(a), 2):   # выбираем только четный индекс
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# # for i in range(1, len(a)):
# #     if a[i] > a[i - 1]:
# #         print(a[i], end=" ")
#
# for i in a:   # не будет работать

#     if i > i - 1:
#         print(i, end=" ")
# n = list(range(21, 41))
# print(n)
# sum1 = sum2 = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         sum1 += 1
# #     else:
# #         sum2 += n[i]
# for i in n:
#     if i % 2 == 0:
#         sum1 += 1
#     else:
#         sum2 += i
# print("кол-во четных", sum1)
# print("Сумма нечетных", sum2)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# sum1 = kol = 0
# for i in a:
#     if a[i] != 0:
#         kol += 1
#     sum1 += a[i]
# print("среднее арифметическое", sum1 / kol)

# lst = [7, 9, 2, 17, 25]
# print(lst)
# lst[0], lst[1] = lst[1], lst[0]  # чисто питон множественное присваивание замена элементов списка
# print(lst)

# срез
# список [strat:stop:step] участок списка
# s = [7, 9, 2, 17, 25, 88, 88, 5, 99, 56, 5]
# print(s)
# print(s[1:4])  # :- оно должно стоять всегда
# print(s[::-1])  # -1 развернули список
# print(s[0:-1])  # до последнего но его не выводит
# print(s[0:-1:-1])
# print(s[-1:0:-1])
# print(s[12:20:]) # ошибки не будет на срезе

# lst = list(range(1,8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[:1])
# print(lst[-1:])
# print(lst[3:4:])
# print(lst[4:7:])
# print(lst[4:7:])
# print(lst[4:1:-1])
# print(lst[2:5:])

# st = "Hello world 123"
# print(st)
# print(st[1:3])  # работает только со строкой
# print(st[::-1])
# sa = "123456"
# print(sa[::-1])
# sa = int(sa)
# sa = sa *10
# print(sa)

# lst = list(range(1, 8))
# print(lst)
# lst[1:3] = [0, 0, 0, 0, 1]
# print(lst)
# lst[1:2] = [20]  # принцип добавление через срез
# print(lst)
# lst[1] = 40  # обращение конкретно к элементу
# print(lst)
# lst[15:16] = [100]
# print(lst)
# print(len(lst))

# Методы списков
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# lst = list(range(1, 8))
# print(lst)
# lst.append(99)  # в конец списка добавление один элемент
# print(lst)
# lst.extend([1, 2, 3])   # в конец списка добавление списка элементов
# print(lst)
# # lst.extend("abc")   # в конец списка добавление списка элементов
# # print(lst)
# lst.insert(3, 100)  # добавляет в список объект в нужный индекс остальное отодвигает
# print(lst)
# # lst.insert(20, 200)
# # print(lst)

# s = []
# n = int(input("Кол-во элементов спмска: "))
# for _ in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)     # заполняем список сначала до конца
#     s.insert(0, x)  # заполнение наоборот
# print(s)

# область пересечения списка
# a = [5, 9, 29, 4, 1, 2, 1, 3]
# b = [4, 9, 1, 6, 5, 1]
# c = []  # вложим в с то что есть в а и совпадает с в

# for i in a:
#     for j in b:
#         if i in c:  # если i находится в с
#             continue
#         if i == j:
#             c.append(i)
#             break
# for element in a:
#     if element in b and element not in c:
#         c.append(element)
# print(c)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# for i in a:
#     if a.count(i) == 1:
#         b.append(i)
# print(b)

# a = [1, 2, 3, 4, 2, 0]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a   # поменять переменные из - за разности длин списков
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])

# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])

# print(c)

# lst = [11, 1, 22, 2, 33, 3, 4, 2, 0]
# print(lst)
# # lst[0:5] = []    # удаление по срезу
# # print(lst)
# del lst[0:5]  # удаление позицию или все
#
# # lst.remove(22)  # удаление из списка по значению первое вхождение
# print(lst)

# last = lst.pop()  # удаляет последнее или указанный элемент его можно сохранить в переменную
# print(last)
# print(lst)
# second = lst.pop(-2)   # удаляет элемент по индексу его можно сохранить в переменную если индекса нет то исключение
# print(second)
# print(lst)
# lst.clear()  # очистили весь список
# print(lst)
# print(" Введите элементы списка")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("вВедите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)

# lst = [11, 1, 22, 2, 33, 3, 4, 2, 0, 33]
# value = 33
# if value in lst:  # проверка есть ли в списке значение
#     ind = lst.index(value, 5, 10)  # возвращает индекс если есть совпадение первое вхождение искомого
#     # значения можно указать диапазон от кого до кого идет поиск, может выбрасываться исключение ValueError = если
#     # элемента нет
#     print(ind)

# lst = [11, 1, 22, 2, 33, 3, 4, 2, 0, 33]
# a = lst.copy()  # копируется список, но ячейки памяти другие
# print(a, id(a))
# print(lst, id(lst))
#
# a.append(100)
# print(a)
# print(lst)
#
# lst[0] = 256
# print(a, id(a))
# print(lst, id(lst))
# print(lst)
# lst.reverse()  # развернуть список
# lst.sort(reverse=True)  # изменяет положение элементов списка изменяет исходный список
# print(lst)
# new_lst = sorted(lst, reverse=True)  # функция не меняет исходный список
# print(new_lst)
# print(lst)
# st = "Hello World"
# print(sorted(st))
# s = ["Виталий", "Сергей", "Александр", "Aнна"]
# s.sort(key=len, reverse=True)   # key= функция
# print(s)

# генерация случайных чисел
# import random  # должен быть всегда в самом вверху

# print(random.random())  # от 0 до 1 не включая 1
# print(random.randint(1, 9))  # генерация случайного числа от a до b включая второе
# print(random.randrange(5,10, 2))  # конечный диапазон не включая шаг целый
# print(random.uniform(1.5, 9.21))  # генерация вещественного числа в диапазоне

# city_list = ["Москва", " новосиб", " Djhjyt", "Сочи", "Екатеренбург"]
# s = [55, 66, 77, 88, 99, 4, 5, 6]
#
# # print(random.choice(city_list))  # возвращает из списка рандомный элемент один
# # print(random.choice(s))
# # print(random.choices(s, k=3))  # вывод заданное кол-во элементов в виде списка
# # print(random.choices(city_list, k=3))
# random.shuffle(city_list)  # перемешает случайным образом и перезаписал списк
# random.shuffle(s)
# print(s)
# print(city_list)
# import random  # должен быть всегда в самом вверху
# mas = [random.randint(0, 100) for i in range(10)]  # генерация случайного списка от 0 до 100 в кол-ве 10
# print(mas)
# print(len(mas))
# print(max(mas))
# print(min(mas))
# print(sum(mas))  # сумма элементов

# import random  # должен быть всегда в самом вверху
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# maxi = max(mas)
# print("Маусимум", maxi)
# mas.remove(maxi)
# print(mas)
# mas.insert(0, maxi)
# print(mas)


# lst = []
# # if len(lst) == 0:
# #     print("Список пустой")
#
# print(bool(lst))    # перевести список в булевый тип данных
# if not lst:     # проверка пустого списка
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

# матрицы
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][1])
# print("Вариант 1")
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# Модули

# import math
#
# print(math.sqrt(3))
# print(math.ceil(3.25)) # округление вверх
# print(math.floor(3.8))  # округление вниз
#
# import math as m  # пример переименовать модуль
#
# print(m.sqrt(3))
# print(m.ceil(3.25)) # округление вверх
# print(m.floor(3.8))  # округление вниз

# from math import *  # все из модуля math * или отдельные функции sqrt, cell
#
# print(sqrt(3))
# print(ceil(3.25))   # округление вверх
# print(floor(3.8))  # округление вниз

# from math import sqrt, ceil, floor      # все из модуля math или отдельные функции sqrt, cell для ускорения загрузки
#
# print(sqrt(3))
# print(ceil(3.25))   # округление вверх
# print(floor(3.8))  # округление вниз

# import math

# print(dir(math))
# from math import pi
#
# print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности", round(2 * pi * radius, 2))
# import time
# # import locale
# #
# # print(time.time())
# # print(time.ctime(10000000000))
# # res = time.localtime()
# # print(res.tm_year, "-0", res.tm_mon, "-0", res.tm_mday, sep='')
# # print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))
#
# locale.setlocale(locale.LC_ALL, "")
# print(time.strftime("Сегодня: %B %d, %Y, %A"))
# 1000000


# import time
#
# start = time.monotonic()
# pause = 5
# print('Программа запущена')
# time.sleep(pause)
# result = time.monotonic() - start
# print('Программа выполнен за', result, 'секунд')

# Функции две строки пустые до функции сначала объявить потом вызвать
# print()
#
#
# def hello(name, age):
#     print("Меня зовут " + name + ". Мне " + str(age) + " лет")
#
#
# hello("Irina", 28)
# hello("Ivan", 15)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x,  y)
# get_sum("abc", "bcd")

# def print_line(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# print_line(9, "+", "-")
# print_line(7, "X", "0")

# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x,  y)
# print(res)
# print(get_sum(x,  y))
#
#
# def func():
#     print('Переменная =', res)
#

# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(9,6))
# print(max_value(9,16))


# def add(x, y):
#     if x > y:
#         print("Разность")
#         return x - y
#     else:
#         print("Сумма")
#         return x + y
#
#
# a = int(input("a= "))
# b = int(input("b= "))
# print(add(a, b))

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst


# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["c", "k", "j", "d"]))

# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# # print(is_first_big(10, 5))
# # print(is_first_big(0, 5))
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if is_first_big(a, b):
#     print("Первое больше второго")
# else:
#     print("Второе больше первого")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":  # проверка всех больших букв,то есть алфавит
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежный пароль")
# else:
#     print("Ненадежный пароль")

# def get_sum(a, b, c=0, d=1):   # значения по умолчанию справа налево нельзя пропустить значение
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 3, 2))
# print(get_sum(1, 5, 3))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# def func(a, b=8):
#     return a + b
#
#
# print(func(2, 5))
# print(func(b=2, a=5))
# print(func(2))

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)
#
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)

# lst1 = [1, 2, 3]  # изменяемый тип данных в той же ячейке памяти
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))
#
# a = "Hello"  # неизменяемый тип данных
# print(a, id(a))
# a = a + "!"  # создание новой переменной и новая ячейка памяти
# print(a, id(a))
#
# a = 5  # неизменяемый тип данных
# print(a, id(a))
# a = a + 3    # создание новой переменной и новая ячейка памяти
# print(a, id(a))

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst[1])
# print(tpl[1])
# lst[1] = 50
# print(lst)
#
# tpl[1] = 50
# print(tpl)

# a = 1, 2, 3, 4, 5
# print(a, type(a))
# a = (1, )  # лучше в скобках
# print(a, type(a))
# a = 1,
# print(a, type(a))
# a = 1
# print(a, type(a))
# a = ()  # но изменить его нельзя
# print(a, type(a))

# a = tuple(Hello)  # преоброзование типа данных
# print(a, type(a))

# a = (1, 2, 3, 4, 5, 6)
# print(a[2])
# print(a[1:3])  # срез

#   print([i for i in range(10)])  # генератор списка
# print(tuple(i ** 2 for i in range(10)))  # генератор кортежа в момент создания можно менять
# #print(tuple(input("->") for i in range(5)))  # генератор кортежа
#
# from random import randint
#
#
# print(tuple(randint(50, 100) for i in range(10)))

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# #   print(t3 * 2)
# print(t3)
# print(len(t3))
# print(t3.count("g"))
# print(t3.index("l",4))

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
#
# for i in t3:
#     print(i,  end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]  # от элемента до конца как срез
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (True, 11, "Python", (4, 5, 6), ["Hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# распаковка кортежа
# t = (1, 2, [2, 4, 3])
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# first_name, yers, married = user

# first_name, yers, married = get_user()
# print(first_name)
# print(yers)
# print(married)
# yers = yers + 2
# print(yers)
# married += 1
# print(married)

# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))
# lst2.append(6)
# tpl2 = tuple(lst2)
# print(tpl2, type(tpl2))

# сложный кортеж
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# # print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ",city_name, ", население = ", city_population, sep="")
#

# tpl = tuple(input("Введите строку: "))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# print(lst)
# for i in range(len(lst)):
#     print("Кол-во", lst[i], " = ", tpl.count(lst[i]))

# Множества (set) - тп данных

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s)
# print(type(s))
# print(len(s))

# a = set("Hellow")
# print(a)
# print(type(a))

# s = {i * i for i in range(10)}
# print(s)

# lst = [10, 10, 5, 5, 5, 1, 2, 6, 5]
# # st = {i for i in lst if i % 2 == 0}  #генератор множества
# # print(st)
# st = set(lst)
# print(st)
# lst2 = list(st)
# print(lst2)

# t = {"red", "yellow", "green", "yellow", "green"}
# print("green" in t)
# print("blue" in t)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print({i for i in lst if "a" in i})
# print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))
# print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])
#
# lst2 = []
# for i in lst:
#     if i[1] == "c":
#         if i[0] == "a":
#             lst2.append("A" + i[1:])
#         else:
#             lst2.append("B" + i[1:])
#
# print(lst2)

# print(dir(set))
# a = {"red", "yellow", "green", "yellow", "green"}
# print(a)
# a.add("black")  # Добавление элемента в set
# print(a)

# a.remove("yellow")   # удаляем элемент по значению
# print(a)
#
# # a.remove("blue")    # KeyError
# el = "red"
# if el in a:
#     a.remove(el)
#
# print(a)
# a.discard("yellow")
# print(a)
# a.discard("blue")  # не выбрасывает исключения если элемента нет в set
# print(a)

# a.pop()  # удаляет первый элемент из множества но какой не знает
# print(a)
#
# a.clear()   # очищает множество
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 2, 3, 1}
# c = a.union(b)  # сложение
# c = a|b  # сложение  {1,2,3,4}
# a |= b  # сокращенное присваивание update #  += -=
# print(a)

# c = a & b  # пересечение множеств используя третью переменную {1,2,3}
# print(c)

# a &= b # пересечение множеств  {1,2,3}
# print(a)

# c = a - b  # элементы которые уникальны и входят в а {0}
# print(c)

# a -= b      # элементы которые уникальны и входят в а {0}
# print(a)

# c = a ^ b  # {0, 4}
# print(c)
# a ^= b  # {0, 4}
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print("Unic element: ", len(s))
# print("Max ", max(s))
# print("Min ", min(s))


# s1 = "Hello"
# s2 = "How are yuo"
#
# a = set(s1) & set(s2)
# print(a)
#
# for i in a:
#     print(i, end=" ")

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}   # в подмножество а
# c = a > b
# print(c)

# frozenset замороженное множество элементы не изменяются и меньше места
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({"Hellow", "world"})
# print(a)

# словарь(dict) изменяемы тип данных
# lst = ["one", "two"]  # есть индексы
# d = {"first": "one", "second": "two"}  # есть значение ключа
# print(lst[1])
# lst[1] = "ten"
# print(lst)
# print(d["second"])
# d["second"] = "ten"
# print(d)

# d = {}
# print(d)
# print(type(d))

# d = dict(c="Hello", b="world")  # преобразование типов данных
# print(d)
# print(type(d))
#
# d1 = {"a": "Hello", "b": "world"}
# print(d1)

# d = {0: "text", "one": 0, (1, 2): [2, 3, 4, 5], 42: [9, 8], True: 1, False:0, "a": [2, 3, 4, 5], 1:"один"}
# # ключом может быть только неизменяемый тип данных ключи должны быть уникальны False = 0 дошел и перезаписал
# print(d)

# user = [
#     ["a", 1],
#     ["b", 2],
#     ["c", 3],
# ]
# print(user)
# new_dict = dict(user)
# print(new_dict)

# d = {i: i ** 2 for i in range(1, 8)}  # генератор словаря
# print(d)
#
# # print(3 in d)  # поиск ключа в словаре
# # print(25 in d)
# del d[3]  # удаляем значение по ключу но удаляется и ключ тоже
# print(d)
# key = 91
# # if key in d:           # удаление  с защитой от исключения
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, " нет в словаре")
# print(d)
#
# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# res = 1
# for key in d:   # приходит только ключ
#     print(key, ":", d[key])
#     res *= d[key]
# print(res)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("->") for i in range(1, 5)}  # генератор заполнения словаря
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {'1': ['Core-i3-4330', 9, 4500],
#          '2': ['Core i5-4670K', 3, 8500],
#          '3': ['AMD FX-6300', 6, 3700],
#          '4': ['Pentium G3220', 8, 2100],
#          '5': ['Core i5-3450', 5, 6400],
#          }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение не корректно. введите число")
#         else:
#             print("Такого ключа нет")
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# методы словарей

# d = {"A": 1, "B": 2, "C": 3, "D": 4}
# print(d)
#
# print(d.keys())  # словарь ключей список
# print(d.values())   # словарь значений список
# print(d.items())    # список ключей и значений в виде кортежа
#
# for i, j in d.items():
#     print(i, ":", j)   # испоьзуется для вывода но не ввод значений
# print(d)

# d = {"A": 1, "B": 2, "C": 3, "D": 4}
# d2 = d.copy()   # копия словаря на разных ячейках памяти
# print(d)
# print(d2)
# d2["B"] = 5
# print(d)
# print(d2)

# d = {"A": 1, "B": 2, "C": 3, "D": 4}
# print(d)
# d.clear()  # clear all values
# d.pop("B")  # del in key
# item = d.pop("B", "Такого ключа нет в словаре")     # если нет даст сообщение, но не ошибку
# print(d)
# print(item)  # сохраняет удаленное значение в ключе
# item = d.popitem()  # удаляет последнее значение и возвращается кортеж из ключа и значения
# print(d)
# print(item)  # удаленное значение

# d = {"A": 1, "B": 2, "C": 3, "D": 4}
# print(d)
# print(d["W"])
# value = d.get("W", "Такого ключа нет")  # получает значение по ключу с защитой от неправльного ключа
# print(value)
# item = d.setdefault("M", 5)  # существующий ключ не меняет значение, но может добавить несуществующий и значение
# print(d)
# print(item)

# d = {"A": 1, "B": 2, "C": 3, "D": 4}
# d2 = {"R": 7, "Q": 9, "B": 6}
# d3 = [("W", 7), ("E", 9)]
# print(d)
# print(d2)
# # d3 = d | d2  # сложение словарей, но нельзя кортежи и списки
# d.update(d2)
# d.update(d3)  # сложение словарей можно сложит список и кортеж
# print(d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new_d = dict()
# # new_d["name"] = d.pop("name")
# # new_d["salary"] = d.pop("salary")
# new_d["name"], new_d["salary"] = d.pop("name"), d.pop("salary")
# print(d)
# print(new_d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}  # изменение ключа его удаляем и записываем новый
# d["location"] = d.pop("city")   # pop удаляет значение по ключу и возвращает значение
# print(d)

# d = {
#     "first": {
#         1: "one",
#         2: "rwo",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         3: "five"
#     }
# }
#
# print(d)
#
# # for x in d:
# #     print(x)
# #     for y in d[x]:
# #         print("\t", y, ":", d[x][y], sep = "")
#
# for x, y in d.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ": ", j, sep="")

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}  # изменение ключа его удаляем и записываем новый
# d["location"] = d.pop("city")   # pop удаляет значение по ключу и возвращает значение
# print(d)
# lst = list(d.items())
# print(lst)
# s = list(lst[1])
# print(s)

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# # print({v: k for k, v in d.items()})  # генератор словаря
# print({k: v for k, v in d.items() if v <= 2})  # два первых элемента в принте замена среза
#
# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# dl = {i: i * 3 for i in s}
# print(dl)

# заполнение словаря из списка ключи слова значения список
# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 35, 60, "four", -20]
#
# d = dict()
# s = None
# for i in lst:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)

# zip() работает с последовательностями и объеденить по одному элементу их но показать тип создаваемого элемента

# d = dict(zip([1, 2, 3], ["one", "two", "three"]))
# print(d)
#
# d = list(zip([1, 2, 3], ["one", "two", "three"], [True, False, True]))
# print(d)

# a = [1, 2, 3]
# b = ["one", "two", "three"]
# d = {k: v for k, v in zip(b, a)}
# print(d)

# a = [1, 2, 3]
# c = list(zip(a))
# print(c)

# двух словарей и вывод по одинаковому ключу
# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()): # items возвращает кортеж и две переменных
#     print(k1, ">-", v1)
#     print(k2, ">-", v2)

# lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*lst)  # *-распаковка в связке с zip
# print(a)
# print(b)


# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 2, 1]
# d = dict(zip(letter, number))
# print(d)

# data1 = list(zip(letter, number))
# print(data1)
# data1.sort()  # по ключам сортировка
# print(data1)
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(number, letter))
# data2.sort()  # по значениям сортировка обманываем
# print(data2)
#
# d3 = {v: k for k, v in data2} # обманываем
# print(d3)

# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 2, 1]
# d = dict(zip(letter, number))
# print(d)
#
# data = sorted(d.items())
# print(data)


# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)
# b = [*a, 4, 5, 6]  # *-распаковка списка
# print(b)

# a = [1, 2, 3]
# print(*a)
#
# one = {"один": 1, "два": 2}
# two = {"три": 3, "четыре": 4}
# print({**one, **two})  # **- для словарей так как два значения как бы удаляют скобки
# print(**one)

# colors = ["red", "yellow","green"]
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
#
# for j, color in enumerate(colors, 10):  # функция нумерации
#     print(j, ") ", color, sep="")

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")

# def func(*args):  # любое принимаемое кол-во значений
#     return args
#
#
# print(func(5))
# print(func(5, 2, 3, 4))
# print(*func(5, 2, 3, 4))
# print(func())


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 8))
# print(summa(1, 2, 3))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))


# def func(a, b, *args):  # позиционный элемент и аргумент и
#     return a, b, args
#
#
# print(func(5,4))
# print(func(5, 1, 2, 3, 4, 5, 6, 7, 8, 9))


# def scores(student, *score):
#     print("student name", student)
#     for i in score:
#         print(i ,end=" ")
#
#
# scores("Igor", 5, 4, 5, 4, 5, 4, 5, 4, 5, 2)
# scores("Ivan", 5, 4, 5, 2)

# def func(**kwargs):  # **-создание неограниченного сиска
#     return kwargs
#
#
# print(func(a=1, b=2, c=3, f="f"))
# print(func())
# print(func(st="python"))


# def info(**data):
#     for k, v in data.items():
#         print(k, ": ", v, sep="")
#     print()
#
#
# info(name="Irina", surname="Vetrova", age=22)
# info(name="Igor", phone=132456, age=28, email="igor@mail.ru")

# student = {}
#
# n = int(input("Кол-во: "))
# s = 0
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("введите балл: "))
#     student[name] = point
#     s += point
# average = s / n
# print("Средний балл: ", average, ". Студенты с баллом выше среднего:", sep="")
# for i in student:
#     if student[i] > average:
#         print(i)

# student = {}
#
# n = int(input("Кол-во: "))
# s = 0
# for i, j in enumerate(range(n),1):
#     name = input(str(i) + "-й студент: ")
#     point = int(input("введите балл: "))
#     student[name] = point
#     s += point
# average = s / n
# print("Средний балл: ", average, ". Студенты с баллом выше среднего:", sep="")
# for i in student:
#     if student[i] > average:
#         print(i)

# def func1(*argc):
#     print(argc[0])
#
#
# def func2(**kwargs):
#     print(kwargs["one"])
#     print(kwargs)
#
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)


# Области видимости (scope)
# name = "Tom"  # глобальная переменная
#
#
# def hi():
#     global name  # превращение локальной в глобальную переменную
#     name = "Sam"
#     surname = "Jonson"   # локальная переменная только в функции
#     print("Hello", name, surname)
#
#
# def bay():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bay()
# print(name)
#
# import builtins
#
# name = dir(builtins)
# for t in name:
#     print(t)

# sum = 5

# lst = [1, 2, 3, 4, 5]
# print(sum(lst))

# x = 4
#
#
# def func():
#     x = 2  # enclosing область видимости
#
#     def inner():
#         print("x = ",x)
#         print(x + 3)
#     print(x)
#     inner()
#
#
# func()

# вложенные функции

# def outer(who):
#     def inner():
#         print("Hello",  who)
#
#     inner()
#
#
# outer("World")

# def fun1():
#     a = 6  # 2
#
#     def fun2(b):
#         a = 4   # 5
#         print("Сумма ", a + b)  # 6
#
#     print("a:", a)  # 3
#     fun2(3)  # 4
#
#
# fun1()  # 1

# x = 25
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a  # сделали не локальной переменной в пределах функции
#         a = 35
#         print("a= ", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 35
#
#         def fn3():
#             # global x
#             nonlocal x  # отправили выше находит ту же переменную но в функции
#             x = 55
#
#         fn3()
#         print("fn2.x= ", x)  # 35
#
#     fn2()
#     print("fn1.x", x)  # 25
#
#
# fn1()
# print(x)

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()
#     return [a, b]


# print(outer(2, 3, -1, 4))


# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(8,6,1))

# Замыкание возвращает вложеную йункцию не вызывая ее
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

# def func1():
#     a = 1
#     b = "Line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         # a = 5
#         # print(a)
#
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     n = 0
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(city, n)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res2()
# res1()
# res1()

#
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


# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(8, 6, 1)
# print(s)


# def outer(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return 2 * s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(8, 6, 1))


# анонимные функции (lambda-выражение)

# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
#
# print(func(1,2))
#
# func = (lambda x, y: x + y)(1, 2)
# print(func)

# print((lambda a, b, c: a + b + c)(10, 30, 20))
# print((lambda a, b, c=3: a + b + c)(10, 30))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))(1, 2, 3, 4, 98))

# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for i in tpl:
#     print(i("abc___"))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(42)
# print(f(3))

# outer = lambda n: lambda x: n + x
# f = outer(42)
# print(f(3))

# print((lambda n: lambda x: n + x)(42)(3))  # не нужно имя для функции лябда простая функция только то что в return

# print((lambda a: lambda b=6: lambda c: a + b + c)(2)()(6))

# лябда может передоваться в качесве аргумента

# d = {"b": 10, "a": 15, "c": 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])  # сортировка по первому значению кортежа
# print(lst)
# print(dict(lst))


# def func(i):
#     return i[1]
#
#
# d = {"b": 10, "a": 15, "c": 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)  # сортировка по первому значению кортежа
# print(lst)
# print(dict(lst))

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item["last name"])
# print(res)
# res = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res)
# res = sorted(players, key=lambda item: item["rating"])
# print(res)

# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(lst[0](12, 6))
# print(lst[1](12, 6))
# print(lst[2](12, 6))
# print(lst[3](12, 6))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
#     }
#
# d[7]()  # обращение к словарю по ключи и вызываем функцию постыми скобками

# print((lambda a, b: a if a > b else b)(5, 3))  # lambda может быть тернальное выражение if_else
#
# from random import randint
#
# print((lambda lst: [randint(10, 20) for i in lst])([1, 2, 3, 4, 5, 6]))

# map(function, iterables) ,  filter(function, iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 0, 18, -5, -10]
# print(tuple(map(mult, lst)))  # map это цикл идет по списку и выполняет функцию и тип данных укажем
# print(list(map(mult, lst)))  # map это цикл идет по списку и выполняет функцию и тип данных укажем
#
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, [2, 0, 18, -5, -10])))

# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(round, t)))
# print(tuple(map(int, t)))  # преобразование в другой тип данных
# print(list(map(str, t)))  # преобразование в другой тип данных

# st = ["a", "b", "c", "d", "e", "w"] # элеменов могло быть больше но их игнорирует
# num = [1, 2, 3, 4, 5]
# print(dict(map(lambda x, y: (x, y), st, num)))
# print(list(map(lambda x, y: (x, y), st, num)))


# st = ["a", "b", "c", "d", "e", "w"]  # элеменов могло быть больше но их игнорирует
# num = [1, 2, 3, 4, 5]
# tpl = (True, False, False, True, False)
#
# print(list(map(lambda x, y, c: (x, y, c), st, num, tpl)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda a, b: a + b, l1, l2)))

# lst = [input("->") for i in range(5)]
# print(lst)
#
# lst = list(map(int, lst))
# print(lst)


# t = ("abcd", "abc", "asdsd", "asd", "dsd", "444", "")
#
# print(tuple(filter(lambda s: len(s) == 3, t)))  # у фильтра возвращается булевое значение есть ли True то идет в новый
# # объест если нет то не учитывается по условию
#
# lst = [66, 99, 68, 56, 48, 60, 88, 77, 65]
# lst1 = list(filter(lambda s: s > 75, lst))
# print(lst1)
# print(lst)

# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda a: 10 <= a <= 20, lst)))

# lst = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: not s % 15, lst)))


# area = {
#     "Круг": lambda x: 3.14 * x ** 2,
#     "Прямоугольник": lambda a, b: a * b,
#     "Трапеция": lambda a, b, h: (a + b) * h / 2,
# }
# r, a2, b2, a1, b1, h1 = 2, 10, 13, 7, 5, 3
# print("Площадь окружности радиуса ", r, ": ", area["Круг"](r), sep="")
# print("Площадь прямоугольника размером ", a2, "*", b2, ": ", area["Прямоугольник"](a2, b2), sep="")
# print("Площадь трапеции a=", a1, " ,b=", b1, " ,h=", h1, ": ", area["Трапеция"](a1, b1, h1), sep="")

# декораторы

# def hello():
#     return "Hello, I am func"
#
#
# def super_func(func):
#     print("Hello, I am super_func")
#     print(func())
#
#
# super_func(hello)  # передаем в функцию имя другой функции и вызываем ее внутри другой


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello  # присвоение переменной функции без () с ними это вызов
# print(test())
# def my_decorator(func):
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#     return func_wrapper    # замыкание
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()
#
# def my_decorator(func):     # декарирющая функция
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#     return func_wrapper    # замыкание
#
#
# @my_decorator    # декоратор @-служебный знак
# def func_test():   # декарируемая функция
#     print("Hello, I am func 'func_test'")


# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold  # чем выше тем ближе
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def outer(fn):
#     def inner(arcs1, arcs2):    # передаем тоже ко-во данных 2 шт во вложенную функцию
#         print("Data", arcs1, arcs2)
#         fn(arcs1, arcs2)
#
#     return inner
#
#
# @outer
# def print_full_name(first, last):  # функция с 2 парметрами
#     print(" Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args", args)
#         print("kwags", kwargs)
#         fn(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="Python",f=5):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_data("Boris", "Lisa", "Sveta", study="JavaScript", f=2)
# print_data("Vova", "Ivan", "Vika")

# def decor(args1,args2):  # максимальное вложение для декоратора 3
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(7, 12)

# def multiply(arg):
#     def my_des(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#         return wrap
#     return my_des
#
#
# @multiply(3)   # так как есть параметр то 3
# def return_num(num):
#     return num
#
#
# print("результат", return_num(5))


# def multiply():
#     def wrap(*args, **kwargs):
#
#         return func(*args, **kwargs) / len(arg)
#
#     return wrap
#
#
# @multiply()  # так как есть параметр то 3
# def return_num(*num):
#     return sum(num)
#
#
# print("результат", return_num(5, 5, 5, 5, 5, ))

# Строки

# print(bin(18))  # 0b10010  - двоичная система нужен префикс
# print(oct(18))  # 0o22  - восмеричная  система
# print(hex(18))  # 0x12- шестнацеричная система
#
# print(0b10010)
# print(0x12 + 0B10010 + 12)

# Unicode

# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)
# print("a" in e)
# print(e[1])
# print(e[-1])
# print(e[1:3])


# def change_char_str(s, old, new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nyton. Мне нравится Nyton. Nyton очень интересный язык программирования "
# str2 = change_char_str(str1, "N", "P")
# print(str1)
# print(str2)

# print("Привет")
# print(u"Привет")

# print("C:\\file.txt\\")
# print(r"C:\file.txt\\")  # r - игнорирование экранирование
# print(r"C:\file.txt\\"[:-1])  # r - игнорирование экранирование
# print(r"C:\file.txt"+"\\")  # r - игнорирование экранирование

# print(b"a1b2c2")  # байтовый вывод строк
# name = "Дмитрий"
# age = 25
# print("Меня зовут", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут" + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age}  лет.")  # f строка дает возможность добавлять переменные в {}

# x = 10
# y = 5
# print(f"{x=}, {y=}")  # f только оператор =
#
# print(f"{x} x {y} / 7 = {round(x * y / 7, 2)}")
# print(f"{x} x {y} / 7 = {x * y / 7:.3f}")

# num = 74
# print(f"{{{{{num}}}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}") # f -для переменных r = для \
# print("home\\" + dir_name+"\\"+file_name) # f -для переменных r = для \

# st = ("Однострочный "
#       "текст")
# print(st)
# s = """Многострочный
# текст
# """
# print(s)
#
# s1 = '''Многострочный
# текст
# '''
# print(s1)
#
# "Коментарий"


# def squware(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n**2
#     return res
#
#
# print(squware(5))
# print(squware.__doc__)
# # print(len.__doc__)
# # print(min.__doc__)
# # print(max.__doc__)
# print(sum.__doc__)

# from math import pi
#
#
# def cylinder(r,h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r+h)
#
#
# print(cylinder(2,4))
# print(cylinder.__doc__)

# print(ord("a"))
# print(ord("П"))
#
# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me "
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]  # ограничили трямя символами и нет в строке
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)
#
# print(chr(97))
# print(chr(35))
# print(chr(999999))

# a = 97
# b = 122
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33  # константы
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Ваш случайный пароль:", random_password())

# Методы строк
# print(dir(str))

# s = "hello, WORLD! I am learning Python"
# print(s.capitalize())   # Hello, world! i am lerning python
# print(s.lower())  # hello, world! i am learning python
# print(s.upper())    # HELLO, WORLD! I AM LEARNING PYTHON

# print(s.count("h", 1,-4))
# print(s.lower().count("i"))

# print(s.find("Python"))
# print(s.find("h", 1, -4))
# print(s.find("h"))
# print(s.rfind("h"))
#
# print(s.index("h"), 1, -4))
# print(s.rindex("h"))


# st = "один два"
# one = st[:st.find(" ")]
# two = st[st.find(" ")+1:]
# print(one)
# print(two)
# res = two + " " + one
# print(res)
# print(st[st.find(" ")+1:] + " " + st[:st.find(" ")])

# s = "hello, WORLD! I am learning Python"
# print(s.startswith("hello"))
# print(s.find("I am"))
# print(s.startswith("I am", 14))
#
# print(s.endswith("Python"))  # определение расширения файла

# print("abc123".isalnum()) # состоит ли строка только из букв или цифр
# print("abc!123".isalnum()) # состоит ли строка только из букв или цифр
# print("abc".isalnum()) # состоит ли строка только из букв или цифр

# print("ABCabc".isalpha()) # состоит ли строка только из букв
# print("A4BCabc".isalpha()) # состоит ли строка только из букв
# print("AДBCabc".isalpha()) # состоит ли строка только из букв

# print("123".isdigit())  # состоит ли строка только из цифр
# print("A123".isdigit())  # состоит ли строка только из цифр

# print("aab".islower())  # есть ли буквы в нижнем регистре, допускается наличие других исмволов
# print("aabУ".islower())  # есть ли буквы в нижнем регистре, допускается наличие других исмволов
# print("aab2".islower())  # есть ли буквы в нижнем регистре, допускается наличие других исмволов
# print("ABC".isupper()) # есть ли буквы в верхнем регистре допускается наличие других исмволов
# print("ABC12".isupper()) # есть ли буквы в верхнем регистре допускается наличие других исмволов

# print("py".center(10))
# print("py".center(10,"-"))
# print("py".center(1))

# print("    py".lstrip())
# print("py    ".rstrip())
# print("    py    ".strip())
#
# print("https://www.python.org".lstrip("/:htps")) # удаляет слева но только до символа который есть
# print("https://www.python.org".strip("/:htps.w")) # удаляет слева но только до символа который есть


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python", 2))  #поиск и замена

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(["1", "99"]))  # только строки
# # print("..".join([1, 99])) # не работает
# print(":".join("Hello"))    # символы азделителя и нет в конце

# s = "Hello"
# print(s[::-1])

# st = "I am learning Python. hello, WORLD!"
# a = st[:st.find("h")]
# b = st[st.find("h"):st.rfind("h") + 1]
# c = st[st.rfind("h") + 1:]
# print(st)
# print(a + b[::-1] + c)

# print("Строка разделенная пробелом".split()) # разделяет по элементу разделения
# print("www.pyton.org.ru".split(".", 2))

# s = input("Введите ФИО:").split()
# print(s)
# print(f"{s[0]} {s[1][0]}.{s[2][0]}.")

# s = input("Введите набор чисел через пробел:").split()
# print(s)
# num = list(map(int, s))
# print(num)
# print(sum(num))

# регулярные выражения

# import re
#
# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789.[Hel_lo] Wor-ld"
# # print(dir(re))
# # reg = "\\."
# reg = r"\."  # точка спецсимвол
# print(re.findall(reg, s))  # возвращает список совпадений с шаблоном
# print(re.search(reg, s))  # возврашает первое совпадение с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.split(reg, s))   # возвращает список символом разделителем можно не один используя []
# print(re.sub(reg,"!", s))   # поиск и замена
# reg = r"[205]"  # покажет все цифры
# reg = r"[0-9]"  # покажет все цифры возвращает один искомый символ
# reg = r"[12][0-9][0-9][0-9]"  # покажет все 4 цифры возвращает
# reg = r"[А-Яа-я]"
# reg = r"[А-яЁё.\]\[-]"  # только русские буквы спец символы экранируем \ и r строка мину выносим
# reg = r"[A-Za-z]"
# reg = r"[^0-9]"  # все кроме цифр ^
# print(re.findall(reg, s))

# reg = r"\d"  # цифры 0-9
# reg = r"\D"  # все кроме цифр
# reg = r"\s"  # пробелы
# reg = r"\S"  # все что не пробелы
# reg = r"\w"  # A-Z a-z А-я 0-9 _
# reg = r"\W"  # ^[A-Z a-z А-я 0-9 _]
# reg = r"\АЯ ищу"  # в начале строки
# reg = r"совпадения\b"  # в конце слова


# import re
#
# st = " Час в 24-формате от 00 до 23. 2021-06-15T28:59. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))

# import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789.[Hel_lo] Wor-ld 20000"
#
# # reg = r"\w+"
# reg = r"20*"
# print(re.findall(reg, s))

# кол=вл повторений
# +  от 1 до бесконечности
# * от 0 до бесконечности
# ? от 0 до 1 повторения

# d = "Цифры: 7, +17, --42, 0013, 0.3"
# reg = r"[+-]?[\d.]+"  # ? относится к []
# print(re.findall(reg, d))

# st = "05-03-1987 # дата рождения"
#
# print("дата рождения:", re.sub(r"\s#.+", "", st))  # что ищем на что меняем и где меняем
# print(re.sub("-", ".", st))
# print("дата рождения:", re.sub(r"\s#.+", "", re.sub("-", ".", st)))

# st = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; yer= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w*\.?\w*\.?"
# # reg = r"\w+\s*=\s*\w+[\s\w\.]*"
# reg = r"\w+\s*=[^;]+"  # [^] все что не точка с запятой любое кол-во раз
# print(re.findall(reg, st))
# print(re.split(r";\s", st))

# st = "12 сентября 2025 год 456 123456789"
# # reg = r"\d{4}"
# reg = r"\d{2,4}"
# # reg = r"\d{,4}"  # 0 .. 4
# # reg = r"\d{4,}" # 4.. do
# print(re.findall(reg, st))

# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789.[Hel_lo] Wor-ld 20000"
# # reg = r"^\w+\s\w+"
# # reg = r"\w+\s\w+$"
# # print(re.findall(reg, s))
#
#
# def validate_login(login):
#     return re.findall(r"^[a-zA-Z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("ytp01234568"))


# import re

# print((re.findall(r"\w+", "12 + й")))
# print((re.findall(r"\w+", "12 + й", flags=re.ASCII)))
#
# text = "hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = "helLo worLd"
# print(re.findall(r"l", text, re.IGNORECASE))  # bигнорирет регистр

# text ="""
# one
# two
# """
#
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL)) # . - любой символ о не перенос а с флагом перенос
#
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))  #в многострочном тексте

# print(re.findall("""
# [a-z.-]+  #part1
# @   #@
# [a-z.]+ #part2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соотвествия регулярных выражений/<body>"
# print(re.findall("<.*?>", text))
#
# st = "12 сентября 2025 год 456 123456789"
# # reg = r"\d{4}"
# # reg = r"\d{,4}?"
# # # reg = r"\d{,4}"  # 0 .. 4
# reg = r"\d{4,}?" # 4.. do
# print(re.findall(reg, st))

# *?, +?, ??
# {m,n}?, {,n}?, {m,}

# s = "Петр, Ольга и Виталий отлично учатся"
# reg = "Петр|Ольга|Виталий|Василий"  # перечень через или
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"int\s*=\s*\d[\w.]*|float\s*=\s*\d[\w.]*"
# reg = r"(?:int|float)\s*=\s*\d[\w.]*"
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r"\s*[+*-]\s*"
# print(re.split(reg, s))
#
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# s = "28-12-1921" # 01 - 31
# reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s))
# print(re.search(reg, s).group())

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE).group(0))
# m = re.search(reg, s, re.IGNORECASE)
# print(m[1])  # Только первую круглую скобку
# print(m[2])  # Только вторую круглую скобку
# print(m[3])

# s = "Самолет прилетает 10/23/2025, Будем рады Вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))  # поменяем местами даты и месяцы и символ между ними

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):
#     if n == 0:  # базовый случай или условия выхода из рекурсии
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)     # стек 5 4 3 2 1 ввыод в обратном порядке
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]   # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:]) # кладет в стек данные 1+3+5+7  но сложит в конце
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):  # n = 254 , base = 10
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # "2"
#     else:
#         return to_str(n // base, base) + convert[n % base]  # to_str(n // base, base) + "4"+"5"
#
#
# print(to_str(254,8))

# рекурсивный обход списка
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))   # проверка типа данных
# print(isinstance(names[1], list))   # проверка типа данных
# print(names[1][1])
# print(isinstance(names[1][1], list))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# # подсчет всех значений
# def count_item(item_list):
#     count = 0
#     for item in item_list:  # adam
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))

# def negative_number(n):
#     if not n:
#         return 0
#     cnt = 0
#     if n[0] < 0:
#         cnt += 1
#     return cnt + negative_number(n[1:])
#
#
# lst = [-2, 3, 8, -11, -4, 6]
#
# print(negative_number(lst))

# print("Hello in local")
# print("new code")

# Работа с файлами

# f = open("text.txt")
# # f = open(r"C:\Users\1\Desktop\pyton\text.txt")
# print(*f)
# print(f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# print(f.closed)
# f.close()
# print(f.closed)

# f = open("text.txt")
# print(f.read(3))
# print(f.read())
# f.close()

# f = open("xyz.txt", "w")  # режим запись
# f.write("This is line 1.\nThis is line 2.\nThis is line 3.\n")
# f.close()

# f = open("xyz.txt")
# # print(f.read())
#
# # print(f.readline())  # чтение одной строки
# # print(f.readline(8))  # чтение одного абзаца или строки
# # print(f.readline())  # чтение одного абзаца или строки
# # print(f.readlines())  # списком строк
#
# f.close()

# f = open("xyz.txt")
# for line in f:
#     print(line)
#
# f.close()

# lines = ["This is line 1.\n", "This is line 2.\n", "This is line 3.\n"]
#
# f = open("lines.txt", "w")
# f.writelines(lines)
# f.close()

# lines = [str(i) for i in range(10, 1000, 15)]
# print(lines)
#
# f = open("lines.txt", "w")
# for index in lines:
#     f.write(index + "\t")
# f.close()


# file = "text2.txt"
# f = open(file, "w")
# f.write("Замена строки в текстовом файле; \nизменить строку в списке; \nзаписать список\n")
# f.close()
#
# f = open(file, "r")
# read_line = f.readlines()   # получили список
# print(read_line)
# read_line[1] = "Hello World!\n"
# print(read_line)
# f.close()
#
# f = open(file, "w")
# f.writelines(read_line)
# f.close()

# f = open("text.txt", "r")
# print(f.read(3))
# print(f.tell())     # условная позиция в файле
# print(f.seek(1))  # перемещает курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text5.txt", "a+")
# print(f.write("I am learning Python"))
# print(f.seek(0))
# print(f.write("--new string--"))
# # print(f.read())
#
# f.close()

# with open("text.txt", "w") as f:
#     print(f.write("0123456789"))
#     print(f.closed)  # файл открыт
# print(f.closed)  # файл закрыт

# lst = [4.5, 2.8, 3.9, 1.8, 0.3, 4.55, 5.01]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
# # print(get_line(lst))
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))
#
# print("Конец программы")

# with open("res.txt") as f:
#     nums = f.read()
#
# print(nums)
# print(map(float, nums.split()))  # переводим в float
# print(list(map(float, nums.split())))
# print(sum(map(float, nums.split())))


# with open("res2.txt", "w") as f:
#     f.write("Файл — именованная область данных на носителе информации, используемая как базовый объект  "
#             "с данными в операционных системах.")   #взаимодействия
#
#
# def longest_words(file):
#     with open(file) as text:
#         w = text.read().split()  # split разбивает строку по символу пробела и помещает в список
#         print(w)
#         max_lenght = len(max(w, key=len))
#         print(max_lenght)
#         res = [word for word in w if len(word) == max_lenght]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words("res2.txt"))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\n
# Строка №8\nСтрока №9\nСтрока №10\n"
# with open("one.txt", "w") as f:
#     f.write(text)
#
# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# import os

# print(os.getcwd())  # путь к текущей директории
# print(os.listdir())  # список файлов и папок рядом с файлом
# print(os.listdir(".."))  # список файлов и папок рядом с файлом
# print(os.listdir(".venv"))  # список файлов и папок рядом с файлом

# os.mkdir("folder")  # создание папки
# os.rmdir("folder") # удаление папки
# os.makedirs("folder1/nest2/nest3")  # создание дерева

# os.remove("xyz.txt") # удалить файл
# os.rename("two.txt", "www.txt") # переименовать
# os.rename("www.txt","folder1/www.txt")  # перенос в заданную папку

# os.rename("text5.txt","folder1/nest2/nest3/text5.txt") # перенос в заданную папку
# os.renames("text4.txt","folder1/nest2/nest/text4.txt") # перенос в несуществующую папку и создает ее

# file = "test3.txt"
# test = "Замена строки в текстовом файле:\nизменить строку в списке;\nзаписать список в файл;\n444\n555\n6666\n"
# f = open(file, "w")
# f.write(test)
# f.close()
#
# f = open(file)
# read_lines = f.readlines()
# f.close()
# pos1 = int(input("pos1 = "))
# pos2 = int(input("pos2 = "))
# if 0 <= pos1 < len(read_lines) and 0 <= pos2 < len(read_lines):
#     read_lines[pos1], read_lines[pos2] = read_lines[pos2], read_lines[pos1]
# else:
#     print("Такой строки нет")
#
# print(read_lines)
# f = open(file, "w")
# f.writelines(read_lines)
# f.close()
# import os

# print(os.walk("folder1"))
# for root, dirs, files in os.walk("folder1", topdown=False):
#     print("root ", root)
#     print("\tdirs ", dirs)
#     print("\tfiles ", files)

# import os.path  # работает с путями
#
# print(os.path.split(r"c:\users\1\desktop\pyton\folder1\nest2\nest3\text.txt"))  # два кортежа
# print(os.path.join(r"c:\users\1\desktop", "pyton", "folder1", "nest2"))
# собирает в путь даже не существующий
# print(os.path.join("nest2", r"c:\users\1\desktop", "pyton", "folder1", ))
# собирает в путь даже не существующий


# создание папки и файлов по указанному пути
# import os
#
# dirs = [r"Work\F1", r"Work\F2\F21"]
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     "Work": ["w.txt"],
#     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, files in files.items():
#     for file in files:
#         file_path = os.path.join(d, file)
#         # print(file_path)
#         open(file_path, "w").close()
#
# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
# подготовливаем
# # путь
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Таокй  тесктв файле {file}")  # f {} запись переменной в тексте
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {"сверху вниз" if topdown else "снизу вверх"}")
#     for root1, directory, file_name in os.walk(root,topdown):
#         print(root1)
#         print(directory)
#         print(file_name)
#     print("-"*50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)
#
# # Work\w.txt
# # Work\F1\f11.txt
# # Work\F1\f12.txt
# # Work\F1\f13.txt
# # Work\F2\F21\f211.txt
# # Work\F2\F21\f212.txt

# import os
# import time
# # print(os.path.exists(r"c:\users\1\desktop\pyton\folder1\nest2\nest3\text.txt"))     # ПРОВЕРКА наличия пути
# # print(os.path.exists(r"c:\users\1\desktop\pyton\folder1\nest\nest3\text.txt"))
# # print(os.path.isfile(r"c:\users\1\desktop\pyton\folder1\nest2\nest3\text.txt"))  # проверка на файл
# # print(os.path.isfile(r"c:\users\1\desktop\pyton\folder1\nest2\nest3"))  # проверка на файл
# # print(os.path.isdir(r"c:\users\1\desktop\pyton\folder1\nest2\nest3"))  # проверка на папку
#
# file = "1.py"
#
# print(os.path.getsize(file))  # размер в байтах
# print(os.path.getatime(file))  # время последнего доступа к файлу
# print(os.path.getmtime(file))  # время последнего изменения файла
# print(os.path.getctime(file))  # время создания файлу в секундах
#
# kb = os.path.getsize(file)
# a = os.path.getatime(file)
# m = os.path.getmtime(file)
# c = os.path.getctime(file)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))  # используем модуль времени
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
# print(kb // 1024)   # в килобайтах


# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
#
# print(p1.x,p1.y )
# p1.x = 10
# p1.y = 20
# # Point.x = 100
# print(p1.x, p1.y )
# print(p1.__dict__)
#
# p2 = Point()
# print(p2.x, p2.y)
# print(Point.__dict__)

# class Point:
#     """Класс для предоставление координат на плоскости"""
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):
#         self.x = x1
#         self.y = y1
#         print("Устанавливаем координаты ")
#
#
# p1 = Point()
# print(Point.__doc__)
# print(type(p1))
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# print(p1.__dict__)
# Point.set_coord(p1, 20, 30)
# print(p1.__dict__)
# p2 = Point()
# p2.set_coord(100, 200)
# print(p2.__dict__)
#
# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):   # устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # получаем новое имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1983", "45-46-98", "Россия", "Мосвка",
#               "Бульварб 1А")
# print(h1.country)
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())

# изменение свойста
# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         # print("Инициализатор для ", self.name, self.surname)
#
#     def __del__(self):
#         print("Удаление экземпляра")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
# del p1
# print()
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)

#   подсчет вызова класса
# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1  # обращение к статической переменной по имени класса
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.count)  # обращение к статическому свойству
# print(p1.count)     # обращение к статическому свойству
# print(p3.count)     # обращение к статическому свойству

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последний")
#         else:
#             print("Работающих роботов осталось", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов", Robot.k)
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов", Robot.k)
# droid3 = Robot("C30-3PO")
# droid3.say_hi()
# print("Численность роботов", Robot.k)
# print("\n\nЗдесь роботы работают\n")
# print("Роботы закончили работу. Давайте их выключим.")
#
# del droid3
# del droid2
# del droid1
#
# print("Численность роботов", Robot.k)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(s):  # private защита внутри класса
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def get_coord_x(self):
#         return self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# p1 = Point("5", 10)
# # print(p1.__dict__)
# #
# # # p1.z = 20  # добавили свойство за пределом класса только в экземпляре
# # # print(p1.__x, p1.__y)
# # p1.__x = 50
# # p1.__y = "abc"
# print(p1.__dict__)
# p1.set_coord(50.5, 100)
# print(p1.get_coord())
# print(p1.__dict__)
# p1.set_coord(50, "abc")
# print(p1.__dict__)
# p1.set_coord_x(500)
# print(p1.__dict__)
# p1.set_coord_y("500")
# print(p1.__dict__)
#
# # p1._Point__x = "abc"
# # print(p1._Point__x)
# # print(p1.__dict__)
# import os
#
# file_path = r"C:\Users\1\Desktop\pyton\Work\w.txt"
# if os.path.exists(file_path):
#     direct, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name} ({direct}) - время последнего доступа {atime}")
# else:
#     print(f"файл {file_path} не существует")

# import math
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(c):  # проверка на число функция защищена о внешней изменения
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):  # элемент закрыт __ обращение только к классу
#             self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         # for i in range (self.__length):
#         #     for j in range(self.__width):
#         #         print("*", end="")
#         #     print()
#         # for i in range(self.__length):
#         #     print("*" * self.__width)
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# r1 = Rectangle(4, 12)
# r1.set_width(9)
# r1.set_length(2)
# print("Длина прямоугольника:", r1.get_length())
# print("Ширина прямоугольника:", r1.get_width())
# print("Площадь:", r1.get_area())
# print("Перемитре", r1.get_perimeter())
# print("Гипотенуза ", r1.get_hypotenuse())
# r1.get_draw()

# class Point:
#     __slots__ = "x", "y"  #   защита
#
#     def __init__(self, x1, y1):
#         self.x = x1
#         self.y = y1
#
#
# p1 = Point(5, 10)
# # p1.z = 1
# print(p1.x, p1.y)
# # print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(c):  # проверка на число функция защищена о внешней изменения
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def __set_coord_x(self, x):
#         print("Выхов __set_coord_x")
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("No")
#
#     def __get_coord_x(self):
#         print("Вызов __get_coord")
#         return self.__x
#
#     def __del_coord_x(self):
#         print("удаление свойства")
#         del self.__x
#
#     x = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# # print(p1.__set_coord_x)
# p1.x = 50 # set
# print(p1.x) # get
# p1.x = "abc" # saet
# print(p1.x) # get
# del p1.x # del
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(c):  # проверка на число функция защищена о внешней изменения
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property  # get метод он пишется первым
#     def x(self):  # имя метода
#         return self.__x
#
#     @x.setter  # set Метод
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("No format")
#
#     @x.deleter  # метода удаления
#     def x(self):
#         del self.__x
#
#     # x = property(__get_coord_x, __set_coord_x, __del_coord_x) важна последовательность
#
#
# p1 = Point(5, 10)
# # print(p1.__set_coord_x)
# p1.x = 50  # set
# print(p1.x)  # get
# p1.x = "abc"  # saet
# print(p1.x)  # get
# del p1.x  # del
# print(p1.__dict__)

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.__old = year
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina",26)
# print(p1.__dict__)
# p1.name = "Igor"
# p1.old = 66
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
#
# print(Point.get_count())
# print(p2.get_count())

# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# ch = Change()
# print(ch.inc(10))
# print(Change.inc(10), Change.dec(10))

class Numbers:
    @staticmethod
    def max(a, b, c, d):
        mx = a
        if b > mx:
            mx = b
        if c > mx:
            mx = c
        if d > mx:
            mx = d
        return mx

    @staticmethod
    def min(*args):
        mn = args[0]
        for i in args:
            if i < mn:
                mn = i
        return mn

    @staticmethod
    def averange(*args):
        return sum(args) / len(args)

    @staticmethod
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


print("Максимальное число", Numbers.max(3, 5, 7, 9))
print("минимальное число", Numbers.min(3, 5, 7, 9))
print("Среднеарифметичкск", Numbers.averange(3, 5, 7, 9))
print("Факториал", Numbers.factorial(5))
