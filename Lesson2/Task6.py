table = []
product = {'название': '', 'цена': '', 'количество': '', 'eд': ''}
n = 0

while True:
    for i in product.keys():
        name = input(f'Введи значение {i}: ')
        product[i] = name
    n += 1
    table.append((n, product))

    print(table)
