with open("file_task6.txt", 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

    study = {}
    for el in lines:
        key, value = el.split(':')
        count = sum(map(int, "".join([el for el in value if el == ' ' or (el >= '0' and el <= '9')]).split()))
        study.update({key: count})

print(study)
