from sys import argv


def salary(*args):
    return args[0] * args[1] + args[2]


if len(argv) == 4:
    input_data = list(map(float, argv[1:]))
    print(f'Заработная плата: {salary(*input_data)}')
else:
    print(f'Необходимо ввести  3 параметра: Часы, Ставка, Премия')

