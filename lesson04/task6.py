from itertools import count, cycle

for i in count(5):
    print(i)

for el in cycle(['***', '+', '----']):
    print(el)
