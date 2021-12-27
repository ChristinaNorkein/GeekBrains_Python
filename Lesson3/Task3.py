def my_func(num_1, num_2, num_3):
    numbers = [num_1, num_2, num_3]
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    print(sum(numbers)-min)


num_1 = float(input('Введи первое число: '))
num_2 = float(input('Введи второе число: '))
num_3 = float(input('Введи третье число: '))

my_func(num_1, num_2, num_3)
