print('Преобразуем секунды в часы, минуты и секунды')
t = int(input('Введи количество секунд: '))

hour = t // 3600
sec = t % 3600
min = sec // 60
sec = sec % 60

print(hour, ':', min, ':', sec)
