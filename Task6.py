from itertools import count, cycle

for el in count(3):
    if el >= 10:
        break
    else:
        print(el)

my_list = ['red', 'blue', 'white', 'black', 'green']
n = 0
for el in cycle(my_list):
    if n > 9:
        break
    print(el)
    n += 1
