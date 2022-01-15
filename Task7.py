import json

with open("fale_task7.json", 'w') as mf:
    with open("file_task7.txt", 'r', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}

        positiv_profit = []
        for key, value in profit.items():
            if int(value) > 0:
                positiv_profit.append(value)
        avg = sum(positiv_profit) / len(positiv_profit)
        avg_profit = {'average_profit': avg}
        json_list = [profit, avg_profit]

        print(json_list)

    json.dump(json_list, mf)
