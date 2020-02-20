translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять',

}
with open('task4_text_in.txt', 'r', encoding='utf-8') as f:
    with open('task4_text_out.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            if translate_dict.get(line.split()[0]):
                output_text = f'{translate_dict[line.split()[0]]} {line.split()[1]} {line.split()[2]}\n'
                f2.write(output_text)
                print(output_text)
