# proceed = int(input('Введите значение выручки: '))
# costs = int(input('Введите значение издержек: '))
proceed = 553023
costs = 215625
if costs > proceed:
    print('Вы работаете в убыток')
else:
    print('Вы работаете с прибылью')
    profit = proceed / costs
    # employee = int(input('Введите количество сотрудников: '))
    employee = 32
    print(f'Рентабельность предприятия составляет: {profit:.1f}')
    print(f'Прибыль на каждого сотрудника составляет: {(proceed - costs) / employee:.2f}')
