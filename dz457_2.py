str_1 = input('Введіть рядок:  ')

if len(str_1) <= 10:
    ending = str_1[-3:].lower()
    mod_str = str_1[:-3]
    midle = (len(mod_str) // 2)
    mod_str = mod_str[:midle] + ending + mod_str[midle:]
    print(mod_str)
else:
    print('Допустима довжина рядка 10 символів')