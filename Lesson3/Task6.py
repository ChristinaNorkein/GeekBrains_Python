def int_func(text, ABC = 'abcdefghijklmnopqrstuvwxyz'):
    text_lower = text.lower()
    if set(text_lower).isdisjoint(ABC) == False:
        print(text_lower.title())
    else:
        input('Буквы должны быть латинскими.')


text = input('Введи слово или фразу латинскими буквами: ')
int_func(text)
