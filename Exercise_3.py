"""str - string - рядок"""
# str_1 = 'frelander!12345'

# print(str_1)
# str_1 = '''fergerwgwsh
# dgwretrhtgrtwetjyhewtq3435yu6jytnhfgbt4y6
# 5jyhyui475jeyrhtsgafewdeih3t5itofvdk
# rfeioh phejr opjfg re[ofkpwrgj3u9t 3fgpl3t9u349t853t34
# ЩФЛХІЗЦЛоуз вщізєлаозущцжко аушпалцу
# ацкужщпо 43хщпо35з9ге03ш98()*)_*№()*;_)'''
#
# print(str_1)

"""Properties"""
"""INDEX"""
#Це властивість рядків за індексом (порядковий номер елемента) отримувати доступ до конкретно зазначеного за номером елементу4
#index - завжди ціле число
#[index] - getitem - отримання елемента за індексом

# str_1 = 'frelander!12345'

# print(str_1[0])
# print(str_1[1])
# print(str_1[2])

# print(str_1[-1])
# print(str_1[-2])

#У не порожнього рядка завжди можна отримати 1й та останній елемент за
# індексами 0 та -1
# print(str_1[0])
# print(str_1[-1])

"""SLICE"""
# str_2 = 'Pheonix pro max xxxxl'
#[index_start : index_finish]
# index_start - індекс елемента рядка з якого почнеться зріз
# index_finish - індекс елемента ДО якого завершиться зріз
#
# print(str_2[0:6])
# print(str_2)

# print(str_2[14:10]) Неможливий зріз рядка

# print(str_2[:16]) #якщо зріз необхідно почата з 0го елемента то можна не вказувати
# print(str_2[10:]) #якщо зріз має продовжуватись включно з останнім елементом то можна не
# зазначати індекс кінця зрізу

# print(str_2[-10 : -3])

#[index_start : index_finish : frequency] - повні зрізи (зрізи з частотою крока)
# index_start - індекс елемента рядка з якого почнеться зріз
# index_finish - індекс елемента ДО якого завершиться зріз
# frequency - це параметр налаштування частоти кроку зріза

# print(str_2[1:16:2])
# print(str_2[:17:4])
# print(str_2[::3])

#Обернений зріз
# print(str_2[-1 : -13 : -1])
# print(str_2[16 : 2 : -1])
# print(str_2[16 : 2 : -5])

"""Immutable type - НЕ змінювана структура даних"""
# str_3 = 'Aldi focus in from douBLE'
# print(str_3[23])
# print(str_3)

#ПЕРЕЗАПИС, перестворення
# str_3 = 'djfkkdjlqwkfjbgnfvklm;fwekejrf g;dv'
# print(str_3)
#
# str_3 = 'LOOL'
# print(str_3)

"""concatination"""
# print('wfhwiof' + "4r7y289r2")

"""duplicate"""
# print('fer' * 3)

"""Додаток до індексів"""
# str_2 = 'Pheonix pro max xxxxl'

# print(str_2[5])

# index_1 = 10

# print(str_2[index_1])
# print(str_2[index_1 + 6])
# print(str_2[index_1 // 2])

"""Iterable -  Перераховуваність"""
# str_4 = 'Pheonix pro max xxxxl ierhgpfow;jghblvsfkndlek;rwtjepghilkfn s.ml/ejnflkv. '
#len() - функція повертає кількість елементів перераховуваної структури
# print(len(str_4))

"""basic fun - базові функції"""
# str_4 = 'holladn 123432 rOSe del palce &^@$%#&*^'
#lower() - функція яка всі літери рядка в копії перетворить на малі
#upper() -функція яка всі літери рядка в копії перетворить на ВЕЛИКІ

# print(str_4.upper())
# print(str_4.lower())
# print(str_4)

# str_4 = str_4.upper()
# print(str_4)

#capitalize() - функція яка всі літери рядка в копії перетворить на малі окрім першої літери яка стане ВЕЛИКОЮ
#title()- функція яка першу літеру кожного слова зробить великою а всі інші малими
# print(str_4.capitalize())
# print(str_4.title())

'''logic functions - логічні функції'''
#isupper() - чи складається рядок з великих літер
#islower() - чи складається рядок з маленьких літер

# str_4 = 'LOL 9i'
# print(str_4.isupper())
# print(str_4[0].isupper())
# print(str_4[-1].islower())

#isalpha()- перевірка рядка на те що він складається тільки з літер
#isdigit() - перевірка рядка на те що він складається тільки з цифр
#isalnum() - перевірка рядка на те що він складається тільки з літер та цифр
#isspace() - перевірка рядка на те що він складається тільки з символів вайтсейсу(пробіли, переходи на новий рядок, знаки табуляції)

# print('''fwhfw\niugfuiwfww oifwh eilh wfkwe\nfiguwhf
# rgergreg
# ebergbergherherhbe\tr  rg\tr eg
# r gr\teg \tr''')

"""Функція пошуку та <<<заміни>>> символі в рядку"""
#replace() - Функція пошуку та <<<заміни>>>
#replace(target_symbol, symbol_change)
# target_symbol - символ який необхідно відшукати
# symbol_change - символ на який буде замінено сивол target_symbol

# str_5 = 'liquid lower pushing bewadosb SHIPINg 12 12 ########/* pumpking pud'
# print(str_5.replace('l', 'L'))
# str_5 = str_5.replace('l', 'L')
#
# print(str_5)

# print(str_5.replace('pu', 'RE'))
# print(str_5.replace('pu', '9'))
# print(str_5.replace('p', '9999999'))

#replace(target_symbol, symbol_change, quantificator)
# target_symbol - символ який необхідно відшукати
# symbol_change - символ на який буде замінено сивол target_symbol)
# quantificator - параметр налаштовує кількість замін зазначениз символів в рядку

# print(str_5.replace('p', 'U', 2))
# print(str_5.replace('##', 'U', 2))

#find(element) - функція пошуку з початку рядка та повернення додатнього індекса елемента
#rfind(element) - функція пошуку з кінця рядка та повернення додатнього індекса елемента

# print(str_5.find('b'))
# print(str_5.rfind('b'))
# print(str_5.find('B')) #якщо символа не існує в рядку то повертає -1

#count(elment) - шукає та підраховує кількість повторів зазначеного елемента
# print(str_5.count('i'))
# print(str_5.count('I'))
"""Приклади"""
# if
# elif
# else

# str_1 = input('Input any string: ')

# if str_1[3].isupper():
#     print("Четверта літера ВЕЛИКА")
# else:
#     print('Нічого немає.')

# if str_1[0:3].isupper():
# if str_1[:3].isupper():
#     print(str_1.upper())
# else:
#     print('Нічого немає.')


# str_1 = 'pola'

# print(str_1.upper())
# str_1 = str_1.upper()

# print(str_1)



