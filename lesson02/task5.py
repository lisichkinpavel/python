# input_number = int(input('Введите число: '))
input_number = 0
rate_list = [7, 5, 3, 3, 2]
result_list = rate_list[:]
for index, value in enumerate(rate_list):
    if input_number > value:
        result_list.insert(index, input_number)
        break
else:
    result_list.append(input_number)
print(result_list)
