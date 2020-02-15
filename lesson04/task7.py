def fact_gen(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


for idx in fact_gen(15):
    print(idx)
