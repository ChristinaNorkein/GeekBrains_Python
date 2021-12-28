def number_div():
    num_1 = int(input('Введи первое число: '))
    num_2 = int(input('Введи второе число: '))
    if num_2 == 0:
        return('Нельзя делить на 0')
    else:
        div = num_1 / num_2
        return div


print(number_div())
