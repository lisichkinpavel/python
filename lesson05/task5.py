import random
with open('task5_text.txt', 'w', encoding='utf-8') as f_write:
    number_list = [random.randint(1, 99) for i in range(10)]
    f_write.write(' '.join(map(str, number_list)))

with open('task5_text.txt', 'r', encoding='utf-8') as f_read:
    data = f_read.read().split()
    print(f'Сумма всех чисел: {sum(list(map(int, data)))}')
