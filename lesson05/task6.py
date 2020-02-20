output_dict = {}
symbols_to_delete = [':', '(л)', '(пр)', '(лаб)', '—']


def useless_symbols(input_string, *symbols):
    for symbol in symbols:
        input_string = input_string.replace(symbol, '')
    return input_string


with open('task6_txt.txt', 'r', encoding='utf-8') as f:
    for line in f:
        edited = useless_symbols(line, *symbols_to_delete)
        key, *val = edited.split()
        output_dict[key] = sum(list(map(int, val)))

print(output_dict)
