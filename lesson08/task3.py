class InputNumbers(Exception):
    pass


def number_list():
    numbers = []
    while True:
        item = input('Введите число для добавления в список или stop для завершения: ')
        if item.lower() == 'stop':
            break
        else:
            try:
                numbers.append(int(item))
            except Exception as e:
                print(f'Ошибка ввода {e}')
                print(f'{item} должен быть числом')
                continue

    return numbers


print(number_list())
