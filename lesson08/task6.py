class Warehouse:
    items_in_stock = 0
    warhouse_content = []

    @staticmethod
    def set_devices():
        while True:
            name = input('Введите тип устройства: ')
            try:
                quantity = int(input('Введите количество товара: '))
            except ValueError:
                print('Нужно вводить число')
                continue
            price = input('Введите цену товара: ')
            manufacturer = input('Введите производителя товара: ')
            Warehouse.warhouse_content.append({
                'Устройство': name,
                'Количество': quantity,
                'Цена': price,
                'Производитель': manufacturer,
            })
            Warehouse.items_in_stock += quantity
            question = input('Внести в список новый товар? y/n ')
            if question.lower() == 'y':
                continue
            else:
                break
        print(Warehouse.warhouse_content)
        print(Warehouse.items_in_stock)


class Devices:
    def __init__(self, quantity, price, manufacturer):
        self.quantity = quantity
        self.price = price
        self.manufacturer = manufacturer


class Printer(Devices):
    def __init__(self, print_type, quantity, price, manufacturer):
        super().__init__(quantity, price, manufacturer)
        self.print_type = print_type


class Scaner(Devices):
    def __init__(self, scan_resolution, quantity, price, manufacturer):
        super().__init__(quantity, price, manufacturer)
        self.scan_resolution = scan_resolution


class Copier(Devices):
    def __init__(self, copy_speed, quantity, price, manufacturer):
        super().__init__(quantity, price, manufacturer)
        self.copy_speed = copy_speed


Warehouse.set_devices()
