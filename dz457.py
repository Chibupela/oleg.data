str_1 = input('Введіть рядок:  ')

if 5 <= len(str_1) <= 15:
    midle = (len(str_1) // 2)
    first_half = str_1[:midle]
    second_half = str_1[midle:]

    mod_second_half = second_half[:-3] + second_half[-3:].upper()

    mod_str = mod_second_half + first_half
    print(mod_str)
else:
    print('Допустима довджина рядка від 5 до 15 символів')

