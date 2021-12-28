# # С использование оператора **
# def my_func(x, y):
#     return (x ** y)

# С использованием цикла
def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res


x = int(input('Введи положительное число: '))
y = int(input('Введи отрицательное число: '))

print(my_func(x, y))
