item_index = 1
my_warehouse = []

while True:
    name = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    item = input('Введите количество товара: ')
    count = input('Введите единицу измерения товара: ')
    new_dict = {'название': name, 'цена': price, 'количество': item, 'eд': count}
    my_warehouse.append((item_index, new_dict))
    item_index += 1
    ask = input('Добавить еще один товар? (да/нет): ')
    if ask == 'да':
        continue
    else:
        break

# my_warehouse = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#                 (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#                 (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]

name_list = []
price_list = []
items_list = []
count_list = []

for key, value in my_warehouse:
    name_list.append(value.get('название'))
    price_list.append(value.get('цена'))
    items_list.append(value.get('количество'))
    count_list.append(value.get('eд'))

my_dict = {
    'название': name_list,
    'цена': price_list,
    'количество': items_list,
    'ед': count_list,
}
print(my_dict)
