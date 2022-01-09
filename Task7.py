from itertools import count
from math import factorial

def fac():
    for el in count(1):
        yield factorial(el)


max = int(input('Введи целое число: '))
n = 0

for el in fac():
    if n >= max:
        break
    else:
        n += 1
        print(f'{n}! = {el}')
