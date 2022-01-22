trans_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("file_task4_ru.txt", 'w', encoding='utf-8') as w_f:
    with open("file_task4.txt", 'r', encoding='utf-8') as r_f:
        w_f.write(str([line.replace(line.split()[0], trans_dict.get(line.split()[0])) for line in r_f]))
