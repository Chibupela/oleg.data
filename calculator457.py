num_1 = float(input('Input the first number: '))
action = input('Input the action(/, *, -, +, **, //, %): ')
num_2 = float(input('Input the second number: '))

if action == '+':
    print(num_1 + num_2)
elif action == '-':
    print(num_1 - num_2)
elif action == '/':
    if num_2 != 0:
            print(num_1 / num_2)
    else:
        print('іди спи вася на 0 ділити не можна')
elif action == '*':
    print(num_1 * num_2)
elif action == '//':
    if num_2 != 0:
        print(num_1 // num_2)
    else:
        print('іди спи вася на 0 ділити не можна')
elif action == '**':
    print(num_1 ** num_2)
elif action == '%':
    if num_2 != 0:
        print((num_1 / num_2) * 100)
    else:
        print('неможливо виконати дію')
else:
    print('неправильно записані дані')
input()
