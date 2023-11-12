from pywebio.input import input as pw_input
from pywebio.output import put_success

food = pw_input(str('Яка ваша улюблена страва: '))
result = f'О, я теж люблю {food} 😀'
put_success(result)



input()

