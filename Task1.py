from sys import argv

def finance():
    hour = float(argv[1])
    salary = float(argv[2])
    bonus = float(argv[3])
    print(f'Доход за отработанное время равен: {hour * salary + bonus}')

finance()
