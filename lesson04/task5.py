from functools import reduce
sourse_list = [i for i in range(100, 1001) if i % 2 == 0]
print(sourse_list)
print(reduce(lambda x, y: x * y, sourse_list))
