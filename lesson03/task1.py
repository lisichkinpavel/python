def division(num, div):
    try:
        return f'Частное чисел {num} и {div}: {num / div}'
    except ZeroDivisionError:
        return f'На ноль делить нельзя!'


print(division(3, 5))
print(division(3, 0))
