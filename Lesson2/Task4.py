my_list = input('Введи несколько слов: ').split()

for ind, el in enumerate(my_list):
    print(ind, el[:10])
