with open('task1_out.txt', 'w', encoding='utf-8') as f:
    while True:
        input_text = input('Введите текст: ')
        f.write(f'{input_text}\n')
        if not input_text:
            break
