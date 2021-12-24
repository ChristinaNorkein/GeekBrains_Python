my_list = []

for i in range (7):
    a = input('Введи число: ')
    my_list.append(a)

print(my_list)

my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)
