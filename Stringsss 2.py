str_1 = input('Введіть перший рядок: ')
str_2 = input('Ведіть другий рядок: ')
str_3 = input('Введіть третій рядок: ')

str_list = (str_1 + str_2 + str_3)

longest_string = max(str_1, str_2, str_3, key=len)

print('Найдовший рядок:', longest_string)