# time_in_seconds = int(input('Введите время в секундах: '))
time_in_seconds = 55637
hh = time_in_seconds // 3600
mm = (time_in_seconds % 3600) // 60
ss = time_in_seconds % 60
print(f'{hh:02}:{mm:02}:{ss:02}')
