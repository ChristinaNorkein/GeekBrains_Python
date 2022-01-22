my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)

my_set = [el for el in my_list if my_list.count(el) == 1]
print(my_set)

#При использовании множества не сохраняется изначальная последовательность
set_all = set()
set_uniq = set()

for el in my_list:
    if el not in set_all:
        set_all.add(el)
        set_uniq.add(el)
    else:
        if el in set_uniq:
            set_uniq.remove(el)
print(set_uniq)
