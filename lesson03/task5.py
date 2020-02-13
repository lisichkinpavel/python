quit_flag = None
result_sum = 0
while quit_flag != 'q':
    input_string = input("Введите числа или 'q' для завершения: ")
    quit_flag = input_string.split(' ')[-1]
    if quit_flag != 'q':
        result_sum += sum(map(int, input_string.split(' ')))
    else:
        result_sum += sum(map(int, input_string.split(' ')[:-1]))
    print(result_sum)
