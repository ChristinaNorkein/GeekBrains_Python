# Я не понимаю почему вот это решение отрабатывает у меня 6 раз!
# def get_data(user_data):
#     for key, value in user_data.items():
#         print(f'Привет! Твое имя {value}, фамилия - {value}, год рождения {value}, город {value}. Контакты: email - {value} и телефон - {value}')
#
#
# user_data = {}
# fields = ('имя', 'фамилия', 'год рождения', 'город', 'email', 'телефон')
# for field in fields:
#     user_data[field] = input(f'Введи значение поля {field}: ')
#
# get_data(user_data)


def get_data(**kwargs):
    return (f'Привет! Твое имя {name}, фамилия - {last_name}, год рождения {year}, город {city}. Контакты: email - {email} и телефон - {phone}')


name = input('Введи имя: ')
last_name = input('Введи фамилию: ')
year = input('Укажи год рождения: ')
city = input('Укажи город: ')
email = input('Введи email: ')
phone = input('Введи номер телефона: ')

print(get_data(name=name, last_name=last_name, year=year, city=city, email=email, phone=phone))
