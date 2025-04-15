# num = int(input("Ввести множитель: "))
# for i in range(1, 11):
#     print(num, "*", i, "=", num * i)
# import nt
# from tkinter.font import names
# from operator import index
# from operator import index


# print("Угадай число от 1 дл 500")
# import random
#
# num_comp = random.randrange(1, 500, 1)
# print(num_comp)
#
# from datetime import datetime, timedelta
#
# time_now = datetime.now().strftime("%H:%M:%S")
# print(time_now)
# i = 1
# num_user = int(input("Введите число: "))
# if num_user == num_comp:
#     print("Угадали", num_comp)
# else:
#     while num_user != num_comp and num_user != 0:
#         if num_user > num_comp:
#             print("Ваше число больше")
#         else:
#             print("Ваше число меньше")
#         num_user = int(input("Введите число: "))
#         i += 1
#         if num_user == num_comp:
#             print("Угадали", num_comp)
#             print("Пытались", i, "раз")
# if num_user == 0:
#     print("До свидания!")

# first = int(input("Введите начало диапазона: "))
# last = int(input("Введите конец диапазона: "))
# user_num = int(input("введите Ваше число: "))
# while user_num < first or user_num > last:
#     print("Число вне диапазона")
#     user_num = int(input("введите Ваше число: "))
# for i in range(first, last+1):
#     if i == user_num:
#         print("!", i, "!", sep="",end=" ")
#     else:
#         print(i, end=" ")

# lst = list(range(1, 8))
# print(lst)
# lst.extend([9, 10])
# print(lst)
# lst.pop()
# print(lst)

# lst = [10, 20, 10, 20, 30, 40, 30, 50]
# new_lst = []
# for element in lst:
#     if element not in new_lst:
#         new_lst.append(element)
# print(new_lst)

# numbers = []
# squares = []
# cubes = []
# for i in range(1, 11):
#     numbers.append(i)
#     squares.append(i**2)
#     cubes.append(i**3)
# print(numbers)
# print(squares)
# print(cubes)

# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst.reverse()
# print(lst)

# lst = [11, 22, 33, 44, 55]
# for element in lst:
#     if element % 2 == 0:
#         lst.remove(element)
# print(lst)

# lst_1 = [1, 2, 3, 4]
# lst_2 = [5, 6, 7, 8]
# lst_3 = []
# for i in range(len(lst_1)):
#     lst_3.append(lst_1[i] + lst_2[i])
# print(lst_3)
# lst_3.clear()
# for i, j in zip(lst_1, lst_2):
#     lst_3.append(i + j)
# print(lst_3)

# vek_1 = [1, 2, 3, 4]
# vek_2 = [5, 6, 7, 8]
# sk = 0
# for i, j in zip(vek_1, vek_2):
#     sk += i*j
# print("Первый вектор: ", vek_1)
# print("Второй вектор: ", vek_2)
# print("Скалярное произведение:", sk)

# lst = list(range(11))
# print(lst)
# lst.reverse()
# print(lst[::-1])

# lst = list(range(11))
# lst[0], lst[-1] = lst[-1], lst[0]
# print(lst)

# lst = [55, 62, 5, 2, 5, 3, 87, 92]
# lst.sort()
# lst.reverse()
# print(lst)

# lst = [55, 62, 5, 2, 5, 3, 87, 92]
# print(max(lst))
# print(max(lst)/len(lst))

# lst = ["qwe", "qwerty", "sdf", "fdg", "gkld", "a", "gggkotyu"]
# lst1 = []
# g = len(max(lst, key=len))
# for element in lst:
#     lst1.append(element.ljust(g, '_'))   # выравнивание строк и заполнение остаток символом
# print(lst1)

# def tpl_sort(tpl):
#     for _ in tpl:
#         if not isinstance(_, int):
#             return tpl
#     return tuple(sorted(tpl))
#
#
# print(tpl_sort((2, 5, 1, "a")))
# print(tpl_sort((2, 5, 1)))


# def slicer(tpl, element):
#     if element in tpl:
#         if tpl.count(element) > 1:
#             first = tpl.index(element)
#             print(first)
#             second = tpl.index(element, first + 1)
#             print(second)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(element):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 8, 5, 3, 2, 3), 0))
# print(slicer((1, 2, 8, 5, 3, 2, 3), 8))
# print(slicer((1, 2, 8, 5, 3, 2, 3), 2))

# def sieve(tpl):
#     tpl1 = []
#     # for _ in list(tpl):
#     #     if _ not in tpl1:
#     #         tpl1.append(_)
#     [tpl1.append(_) for _ in tpl if _ not in tpl1]
#     return tuple(reversed(tpl1))
#
#
# print(sieve((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7)))


# def del_from_tuple(tpl, element):
#     lst = list(tpl)
#     if element in tpl:
#         lst.remove(element)
#     return tuple(lst)
#
#
# print(del_from_tuple((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7), 5))
# print(del_from_tuple((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7), 1))
# print(del_from_tuple((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7), 0))
# print(del_from_tuple((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7), 2))

# def zam(tpl, k):
#     lst = []
#     for i in tpl:
#         lst.append(i)
#         lst.append(k)
#     return tuple(lst)
#
#
# print(zam((1, 2, 3, 4, 5, 7), 0))
# print(zam((1, 2, 3, 4, 5, 7), "hh"))


# def zam_1(tpl_1, kop):
#     if not tpl_1:
#         print("*")
#         return []
#     else:
#         print(tpl_1)
#         print([tpl_1[0],kop])
#         print(tpl_1[1:])
#
#         return [tpl_1[0], kop] + zam_1(tpl_1[1:], kop)
#
#
# # print(zam_1((1, 2, 3, 5), "ko"))
# print(zam_1((2, 6, 9, 8, 9, 98, 98, 98, 98), "ko"))

# # initializing tuple
# test_tup = (5, 6, 7, 4, 9)
#
# # printing original tuple
# print("The original tuple is : ", test_tup)
#
# # initializing K
# K = "Gfg"
#
# # list comprehension for nested loop for flatten
# res = [ele for sub in test_tup for ele in (sub, K)]
#
# # printing result
# print("Converted Tuple with K : ", res)

# def diff(mn_1, mn_2, mn_3, symmetric):
#     if symmetric:
#         return print(mn_1 ^ mn_2 ^ mn_3)
#     else:
#         return print(mn_1 - mn_2 - mn_3)
#
#
# diff({3, 4, 5, 6, 20}, {4, 6, 7, 8, 9}, {5, 3, 8, 1}, True)
# diff({3, 4, 5, 6, 20}, {4, 6, 7, 8, 9}, {5, 3, 8, 1}, False)


# def superset(set1, set2):
#     if set1 > set2:
#         print("супермножество ", set1)
#     elif set2 > set1:
#         print("супермножество ", set2)
#     elif set2 == set1:
#         print("множества равны")
#     else:
#         print("Супермножество не обнаружено")
#
#
# set_1 = {1, 8, 3, 5}
# set_2 = {3, 5}
# set_3 = {5, 3, 8, 1}
# set_4 = {90, 100}
# superset(set_1, set_2)
# superset(set_1, set_3)
# superset(set_2, set_3)
# superset(set_4, set_2)
#
# def set_gen(lst):
#     ind = 0
#     while ind < len(lst):
#         cnt = lst.count(lst[ind])
#         if cnt > 1:
#             lst[ind] = str(lst[ind]) * cnt
#         ind += 1
#
#     return set(lst)
#
#
# list_1 = [1, 1, 3, 3, 1]
# list_2 = [5, 5, 5, 5, 5, 5, 5]
# list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
# print(list_1)
# print(set_gen(list_1))
# print(set_gen(list_2))
# print(set_gen(list_3))

# def to_dict(lst):
#     return {el: el for el in lst}
#
#
# print(to_dict([5, 5, 5, 5, 5, 5, 5]))
# print(to_dict([2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]))

# my_dict = {'first_one': 'we can do it'}
#
#
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
#
#
# biggest_dict(k1=22, k2=31, k3=11, k4=91)
# biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
# print(my_dict)

# def count_it(sequence):
#     num_frequency = {int(item): sequence.count(item) for item in sequence}
#     print(num_frequency)
# # Сортируем словарь по значениям в порядке возрастания. Для этого методом items() формируем пары “(ключ, значение)”
#     # в виде кортежей по всем элементам словаря. Т. к. нужно сортировать по значениям, берем второй элемент кортежей.
#     # В результате получим список из кортежей “(ключ, значение)”
#     sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
#     print(sorted_num_frequency)
#  # Возвращаем последние 3 элемента списка, т. е. кортежи с самыми большими значениями второй
#     # компоненты, которые преобразовываем в словарь
#     return dict(sorted_num_frequency[-4:])
#
#
# print(count_it('123456789012133288776655353535353441111'))

# lat = {1: "AEIOULNSTR", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
# cyr = {1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ", 4: "ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ"}
# text = input("Введите слово: ").upper()
# if "А" <= text <= "Я":
#     print(sum([k for i in text for k, v in cyr.items() if i in v]))
# else:
#     print(sum([k for i in text for k, v in lat.items() if i in v]))

# num, res, res1 = 123421, 0, 0
# for i in range(6):
#     if i < 3:
#         res += num % 10
#         num = num // 10
#     else:
#         res1 += num % 10
#         num = num // 10
# if res == res1:
#     print("Счастливое шестизначное число")
# else:
#     print("Несчастливое шестизначное число")
# print(res)
# print(res1)
# крестики нолики
# board = list(range(1, 10))
#
#
# def draw_board(num):
#     print("-" * 13)
#     for i in range(3):
#         print("|", num[0 + i * 3], "|", num[1 + i * 3], "|", num[2 + i * 3], "|")
#         print("-" * 13)
#
#
# draw_board(board)
#
#
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token + "? ")
#         try:
#             player_answer = int(player_answer)
#         except ValueError:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if 1 <= player_answer <= 9:
#             if str(board[player_answer - 1]) not in "XO":
#                 board[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка уже занята!")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9.")
#
#
# take_input("X")
