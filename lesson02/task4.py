# input_text = input('Введите слова через пробел:')
input_text = 'Замечательная погода и великолепное настроение'
for index, value in enumerate(input_text.split(' '), 1):
    print(index, value[:10])

