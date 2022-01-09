from functools import reduce

def mult(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)

print(reduce(mult, my_list))
