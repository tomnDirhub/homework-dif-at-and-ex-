class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(*args)
        return super().__new__(cls)


    def __init__(self, *args, qt_of_floors = None):
        self.name = args
        self.qt_of_floors = qt_of_floors

    def go_to(self, new_floor):
        if new_floor > self.qt_of_floors or new_floor < 1:
            print("Введенного этажа не существует")
        else:
            print("Этажи, пройденные вами:")
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.qt_of_floors

    def __str__(self):
        return f"Название: \"{self.name}\", количество этажей: {self.qt_of_floors}"

    def __lt__(self, other):
        return self.qt_of_floors < other.qt_of_floors

    def __gt__(self, other):
        return self.qt_of_floors > other.qt_of_floors

    def __eq__(self, other):
        return self.qt_of_floors == other.qt_of_floors

    def __le__(self, other):
        return self.qt_of_floors <= other.qt_of_floors

    def __ge__(self, other):
        return self.qt_of_floors >= other.qt_of_floors

    def __ne__(self, other):
        return self.qt_of_floors != other.qt_of_floors

    def __add__(self, value):
        self.qt_of_floors = self.qt_of_floors + value
        return self

    def __iadd__(self, value):
        self.qt_of_floors += value
        return self

    def __radd__(self, value):
        self.qt_of_floors = value + self.qt_of_floors
        return self

    def __del__(self):
        print(f"{self.name} снесён, но навсегда останется в истории")

kwargs = {}

bui1 = House('Библиотека', qt_of_floors=12)
bui2 = House("Спортзал", qt_of_floors=4)
print(House.houses_history)
print(bui1)
del bui1

bui3 = House("Бассейн", qt_of_floors=5)

print(House.houses_history)
print(bui2)

