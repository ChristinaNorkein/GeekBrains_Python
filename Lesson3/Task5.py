def numbers_sum():
    while True:
        if input('Нажми Enter. Чтобы прекратить нажми Q и Enter.').upper() == 'Q':
            break

        numbers = input('Вводи числа через пробел: ').split()
        int_numbers = [int(i) for i in numbers]
        print('Сумма всех чисел равна:', sum(int_numbers))


numbers_sum()
