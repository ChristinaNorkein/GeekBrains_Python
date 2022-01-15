with open("file_task1.txt", 'w+') as f:
    while True:
        new_text = input('Внеси новые данные в файл: ')
        f.write(new_text + '\n')
        if not new_text:
            print('Ввод данных завершен.')
            break
