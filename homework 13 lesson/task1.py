# Создать три отдельных объекта: City, Street, House.
# У города должны быть улицы (City -> [Street]), у улиц должны быть дома Street -> [House].
# У города есть улицы и дома и возможности их добавлять и удалять.
#    Улицы могут вместить случайное количество домов от 5 до 20.
#    Дома могут иметь случайное количество населения от 1 до 100.
#    Должна быть возможность наполнить город одним методом.
#    У города должен быть метод который вернет количество населения.
from random import randint


class City:
    def __init__(self):
        self.streets = []

    """
    класс Сити, при создании имеет пустой список улиц. Функция create_streets(self) - наполняет город улицами.
    """
    def create_streets(self):
        for i in range(randint(1, 100)):
            self.streets.append(Street(i))

    @property
    def population(self):
        population = 0
        for street in self.streets:
            for house in street.houses:
                population += house.num_citizens
        return population

    def present_city(self):
        """
        функция, чтоб распечатать в столбики в каком доме на какой улице сколько живет народу.
        """
        print('# street', '\t', '# house', '\t', 'people living in:')
        for street in self.streets:
            for house in street.houses:
                print(f'{street._id} \t\t\t {house.id} \t\t\t {house.num_citizens}')


class Street:
    def __init__(self, _id):
        """
        класс Стрит, при создании имеет пустой список домов. Функция create_houses(self) - наполняет улицу домами.
        """
        self._id = _id
        self.houses = []
        self.create_houses()

    def create_houses(self):
        for i in range(randint(5, 20)):
            self.houses.append(House(i))


class House:
    def __init__(self, id):
        """
        класс Хаус, при создании рандомно генерится num_citizens от 1 до 100 жителей.
        """
        self.id = id
        self.num_citizens = randint(1, 100)


odessa = City()
odessa.create_streets()

print('City population is: ', odessa.population)

odessa.present_city()

