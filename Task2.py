with open("file_task2.txt", 'r') as f:
    line_count = 0
    word_count = 0
    for line in f:
        line_count += 1

        word_count = len(line.split())
        print(f'Количество слов в строке {line_count}: {word_count}')

print(f'Количество строк в файле: {line_count}')
