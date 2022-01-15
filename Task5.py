with open("file_task5.txt", 'w+') as f:
    new_text = input('Введи несколько чисел через пробел: ')
    f.write(new_text)
    f.seek(0)
    result = sum(map(int, f.readline().split()))
    print(result)
