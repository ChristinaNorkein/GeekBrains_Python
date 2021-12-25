my_list = [42, 23, 16, 15, 8, 4]
print(my_list)

while True:
    x = int(input('Введи новое значение: '))
    my_list.append(x)
    print(sorted(my_list, reverse=True))
