import random
input_list = [random.randint(0, 99) for i in range(15)]
# input_list = [2, 61, 36, 5, 99, 1, 68, 16, 95, 13, 99, 38, 6, 58, 98]
result_list = [input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i-1]]
print(input_list)
print(result_list)
