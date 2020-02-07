# input_data = input('Введите элементы списка через пробел: ')
input_data = '1 2 3 4 5 6 7 8 9 10 11'
input_list = input_data.split(' ')
result_list = []
for i in range(len(input_list) // 2):
    result_list.append(input_list[1::2][i])
    result_list.append(input_list[::2][i])
if len(input_list) % 2 != 0:
    result_list.append(input_list[-1])
print(result_list)

