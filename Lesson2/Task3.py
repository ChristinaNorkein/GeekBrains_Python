season = {'осень': [9, 10, 11], 'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8]}

m = int(input('Введи номер месяца: '))

if m <= 0 or m > 12:
    print('В году 12 месяцев. Введи число от 1 до 12.')

for key, value in season.items():
    if m in season.get(key):
        print(key)
