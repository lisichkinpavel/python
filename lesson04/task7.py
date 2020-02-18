def fact_gen(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


for idx, val in enumerate(fact_gen(15), 1):
    print(f'{idx}! : {val}')
