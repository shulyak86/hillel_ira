import csv


class Product:
    def __init__(self, prod_inf, prod_type, price):
        """
        класс Продукт, при создании требует инф.о продукте-строка, тип продукта-строка и цену-целое.
        """
        self.prod_inf = prod_inf
        self.prod_type = prod_type
        self.price = price
        if prod_type != 'coffee' and prod_type != 'tea':
            raise NameError('only coffee or tea product types accepted')

    def show_products(self):
        """
        функция красиво показывает продукт.
        """
        print(f'{self.prod_type}: {self.prod_inf},  Цена: {self.price}')

    def prod_type_check(self):
        return self.prod_type

    def pricing(self):
        return self.price

    def prod_inf(self):
        return self.prod_inf


class Store:
    def __init__(self):
        """
        класс Магазин, при создании имеет пустой список продуктов.
        inventory_without_bakery.csv - копия inventory, но без хлебушка, чтоб срабатывало и не било ошибку
        если поменять имя на inventory.csv - то выдаст ошибку, что только кофе/чай можно
        """
        self.products = []

    def import_products(self):
        with open('inventory_without_bakery.csv', encoding='UTF-8') as file:
            file_reader = csv.DictReader(file)
            #row: dict[str, str]
            i = 0
            while i < 5:
                i += 1
                for row in file_reader:
                    self.products.append(Product(row.get('Наименование'), row.get('Тип'), row.get('Цена')))

    def show_assort(self):
        """
        функция шоу_ассортимент спрашивает, только чай или только кофе или вместе - и соответственно выводит что надо)))
        """
        flag = input('enter coffee for just coffee; tea for just tea; blank for all-together:  ')
        for product in self.products:
            if flag == 'coffee':
                if Product.prod_type_check(product) == 'coffee':
                    Product.show_products(product)
            elif flag == 'tea':
                if Product.prod_type_check(product) == 'tea':
                    Product.show_products(product)
            else:
                Product.show_products(product)

    def total_cost(self):
        cost = 0
        for product in self.products:
            cost += int(product.pricing())
        return cost


magaz = Store()
magaz.import_products()
magaz.show_assort()
a = magaz.products[6]
a.show_products()

print(magaz.total_cost())
print(magaz.products[6].prod_inf)


