staff_dict = {}
with open('task3_text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        key, value = line.split()
        staff_dict[key] = float(value)
    for key, value in staff_dict.items():
        if value < 20000:
            print(f'Сотрудник {key} имеет зарплату меньше 20000 ({value})')
    print(f'Средняя зарплата всех сотруднков {sum(staff_dict.values()) / len(staff_dict):.2f}')
