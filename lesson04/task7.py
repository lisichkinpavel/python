import json
firm_dict = {}
profit_dict = {}
with open('task7_text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name = line.split()[0]
        profit = int(line.split()[-2]) - int(line.split()[-1])
        firm_dict[name] = profit


average_list = [value for value in firm_dict.values() if value > 0]
profit_dict['average_profit'] = sum(average_list) / len(average_list)
result_list = [firm_dict, profit_dict]
print(result_list)


with open('result_json.json', 'w', encoding='utf-8') as write_f:
    json.dump(result_list, write_f)
