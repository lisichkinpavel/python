# num = int(input('Введите целое положительное число: '))
num = 358621
max_digit = 0
while num > 0:
    digit = num % 10
    num = num // 10
    if digit > max_digit:
        max_digit = digit
print(f'Самая большая цифра в числе: {max_digit}')
