str_1 = input("Введіть перший рядок: ")
str_2 = input("Введіть другий рядок: ")
str_3 = input("Введіть третій рядок: ")

middle1 = str_1[len(str_1) // 2] if len(str_1) % 2 != 0 else str_1[len(str_1) // 2 - 1: len(str_1) // 2 + 1]
middle2 = str_2[len(str_2) // 2] if len(str_2) % 2 != 0 else str_2[len(str_2) // 2 - 1: len(str_2) // 2 + 1]
middle3 = str_3[len(str_3) // 2] if len(str_3) % 2 != 0 else str_3[len(str_3) // 2 - 1: len(str_3) // 2 + 1]

print("Середина першого рядка:", middle1)
print("Середина другого рядка:", middle2)
print("Середина третього рядка:", middle3)
