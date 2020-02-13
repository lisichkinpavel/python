def my_func(a, b, c):
    my_list = [a, b, c]
    return sum(sorted(my_list)[1:])


print(my_func(5, 4, 8))
