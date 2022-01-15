with open("file_task3.txt", 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

staff = {}
for el in lines:
    key, value = el.split(' ')
    staff.update({key: int(value)})

avg = sum(staff.values()) / len(staff)

min_staff = []
for key, value in staff.items():
    if int(value) < 20000:
        min_staff.append(key)

print(f'Средний доход сотрудников составляет {avg} рублей')
print(f'Список сотрудников с окладом менее 20000 рублей: {", ".join(min_staff)}')
