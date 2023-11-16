"""Variables - змінні"""

# Створення імен змінних

# 1. Ім'я змінної може містити тільки літери англійської абетки
# 26 lower letters a-z
# 26 upper letters A-Z

# = оператор привласнення, або оператор запису чи перезапису в пам'ять
# alo = 34
# Alo = 12
# ALo = 12
# ALO = 44
# aLo = 124
# alO = 1234
# aLO = 42958

# 2. Ім'я змінної може містити цифри але не на початку назви
# 10 digits - 0 : 9
# var1 = 3453
# var2 = 6476354
# var3 = 3534534
# var9999 = 1234243
# f423i = 4395843
# f423i8695 = 4395843

# 3. Ім'я змінної може містити тільки один єдиний символ не літеру і не цифру
# _
# gof_1 = 234
# _gof = 2432
# __gof = 321432
# _____ufj = 45234
# _4 = 42342

# 4. Ім'я змінної може містити максимум 255 символів

# 5. Не бажано створювати імена змінних які ідентичні назвам команд та операторів мови python

# print('wiofweiof')
# print1 = 3425
# Print = 4235325
# print("fwioehioweh fiwehfiowe")


"""#Style of name - стилі імен змінних"""

# Linear - лінійний стиль
# value = 'iogjpfow'
# var = 25323
# name = 3254
# ABSOLUTE = 453

# Not linear - не лінійний стиль (snake case)
# del_1 = 4385934
# Thinker_cad = 'wfijwife'
# l_1 = 3459349

# Camel case - верблюжий стиль
# noName = 4232
# VariableName = 'Nina'
# idName = 3534
# countOfBigLetters = None

# Syntetic style - змішаний стиль
# noName_1 = 'Varta'
# _privateName_forFl = 4532

"""Створюйте імена змінних за сенсом зберігаємих даних"""
# num = 425
# name = "Linda"
# money = 3453

"""Типи змінних - type of variables"""
# Python - мова програмування яка не суворо типізована, але вона динамічно типізована
# num_1 = 1234

"""Чисельний тип даних"""
# int - ціле число -2342 245523  0  543785728  -8723467823
# float - число з плаваючою крапкою(не цыле число) 0.68752  -0.0234324  34.4543  0.0

# chislo_1 = 5434
# drobove = 34.566

# Math action - математичні дії
# / - + *

# // - цілочислене ділення
# % - остача від ділення (mod)
# ** - піднесення до степеня

# print(10 / 3)
# print(10 // 3)
# print(10 / 2)
# print(10 // 2)

# print(2**4)

# print(19 % 4)
# print(100%40)


# print(chislo_1 + drobove)
# print(chislo_1 / drobove)

# chislo_1 = chislo_1 + drobove
# print(chislo_1)

# result = chislo_1 * drobove
# print(result)

# Logic action
# >
# <
# ==
# !=
# >=
# <=

# not - логічне заперечення будь чого
# and - логічний поєднувач (і то і інше)
# or - логічний поєднувач (або то або інше)
# in - пошук одного серед багатьох
# is - оператар порівняння за типом

# print(chislo_1 > drobove)
# print(chislo_1 >= drobove)

# print(chislo_1 > drobove and chislo_1 < 10000)
# print(chislo_1 > drobove and chislo_1 > 10000)

# print(chislo_1 > drobove or chislo_1 > 10000)

"""Логічний тип даних - bolean"""
# bool - логычний тип даних  True(1)   False(0)

'''Рядковий тип даних'''
# str - тип даних для зберігання тексту та символів

# str_1 = 'Liquid money'
# str_1 = '72452387&*@(#&$@(#&%@(#)u j23hoihDE@IOFjls ІІлцщаоівдаоцш уощвіощазлуовршущцадДІ'
# str_1 = '''vnwirh fw
# efh wieghw
# ehf
# we9_@U#R)2uR$
#  420
#  wtuj240tuj24trf24'''

# print(str_1)

# like math action
# str_1 = 'lol'

# конкатенація  +
# print(str_1 + 'Johan')
# print('10' + '78')


# дуплікація  *
# str * int       int * str
# str_1 = 'lol'
# print(str_1 * 3)
# print(10 * str_1)


# Logic action
# >
# <
# ==
# !=
# >=
# <=

# not - логічне заперечення будь чого
# and - логічний поєднувач (і то і інше)
# or - логічний поєднувач (або то або інше)
# in - пошук одного серед багатьох
# is - оператар порівняння за типом


"""Оператор введення даних до консолі"""
# str_inp = input('Input the name: ')
#
# print(str_inp )

# перетворення типів
# num_1 = int(input('Input the integer number: '))
# print(num_1 + 1000)

# num_1 = float(input('Input the float number: '))
# print(num_1 + 1000)


"""ПРИКЛАД застосування"""
num_1 = int(input('Input the first number: '))
action = input('Input the action(/*-+): ')
num_2 = int(input('Input the second number: '))

"""Умовні оператори"""
# if
# elif
# else

# if action == '+':
#     print(num_1 + num_2)
#
# if action == '-':
#     print(num_1 - num_2)


if action == '+':
    print(num_1 + num_2)
elif action == '-':
    print(num_1 - num_2)
elif action == '/':
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print('На 0 ділити не можна, іди вчи математику')
