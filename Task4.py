from googletrans import Translator

with open("file_task4_ru.txt", 'w', encoding='utf-8') as nf:
    with open("file_task4.txt", 'r', encoding='utf-8') as mf:
        data = mf.read()
        print(data)
    trans = Translator()
    data_trans = trans.translate(data)
    print(data_trans)
