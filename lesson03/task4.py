def exponentation(x, y):
    dividor = 1
    for i in range(abs(y)):
        dividor *= x
    return 1/dividor


print(exponentation(3, -4))
print(3 ** -4)
