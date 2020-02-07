# a = int(input('Введите значение a: '))
# b = int(input('Введите значение b: '))
a = 2
b = 3
day_to_reach = 1
while a < b:
    a = a + a * 0.1
    day_to_reach += 1
print(day_to_reach)
