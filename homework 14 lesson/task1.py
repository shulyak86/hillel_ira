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
        self.cash = 0
    def __getitem__(self, item):
        return item


    def import_products(self):
        i = 0
        while i < 5:
            with open('inventory_without_bakery.csv', encoding='UTF-8') as file:
                file_reader = csv.DictReader(file)
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

    def sell(self, selling_good):
        '''
        function sells item. it deletes 1 chosen item from list of items and adds its price to cash.
        :param selling_good: put name of tea or coffee item, you want (Зеленый чай, Имбирный чай, Доппио, Латте..)
        :return:
        '''
        for i in range(len(self.products)):
            if self.products[i].prod_inf == selling_good:
                self.cash += int(self.products[i].pricing())
                del self.products[i]
                break


magaz = Store()
magaz.import_products()
magaz.show_assort()
a = magaz.products[6]

magaz.sell('Earl Grey')
magaz.sell('Earl Grey')
magaz.sell('Earl Grey')
magaz.sell('Earl Grey')
magaz.sell('Earl Grey')
magaz.show_assort()

print('Total cost of items left in shop: ', magaz.total_cost())
#print(magaz.products[6].prod_inf)
print('In our cashier: ', magaz.cash)


