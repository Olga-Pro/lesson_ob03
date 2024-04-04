# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `
# ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    def get_type(self):
        pass

class Bird(Animal):
    def eat(self):
        print("питается семенами и насекомыми")

class Mammal(Animal):
    def eat(self):
        print("в детстве питается молоком")

class Reptile(Animal):
    def eat(self):
        print("питается насекомыми")
class Turtle(Reptile):
    def make_sound(self):
        print("молчит")

    def eat(self):
        print("питается растительной пищей")
    def get_type(self):
        print("Черепаха")
class Serpent(Reptile):
    def make_sound(self):
        print("шшш")

    def eat(self):
        print("питается мелкими грызунами")
    def get_type(self):
        print("Змея")
class Tiger(Mammal):
    def make_sound(self):
        print("ррр")
    def eat(self):
        print("питается мясом")
    def get_type(self):
        print("Тигр")
class Goal(Mammal):
    def make_sound(self):
        print("бее")

    def eat(self):
        print("питается травой")
    def get_type(self):
        print("Коза")
class Elephant(Mammal):
    def make_sound(self):
        print("уууу")

    def eat(self):
        print("питается растительной пищей")
    def get_type(self):
        print("Слон")

class Peacock(Bird):
    def make_sound(self):
        print("очень неприятно кричит")
    def get_type(self):
        print("Павлин")
class Cuckoo(Bird):
    def make_sound(self):
        print("ку-ку")
    def get_type(self):
        print("Кукушка")

class Personal():
    def __init__(self, name, position):
        self.name = name
        self.position = position

class ZooKeeper(Personal):
    def feed_animal(self):
        print("кормит животных")

class Veterinarian(Personal):
    def heal_animal(self):
        print("лечит животных")

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []
    def add_personal(self, person):
        self.staff.append(person)

    def add_animal(self, animal):
        self.animals.append(animal)

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
def animal_sound(list_animals):
    for animal in list_animals:
        animal.get_type()
        animal.make_sound()

animals = [Tiger("Вася", 5), Elephant("Джонни", 50), Serpent("Зоя", 4),
           Goal("Машка", 2), Peacock("Паша", 4), Cuckoo("Кеша", 2), Turtle("Тортилла", 70)]

animal_sound(animals)

#создаем зоопарк
zoo = Zoo()
for animal in animals:
    zoo.add_animal(animal)

staff = [ZooKeeper("Иван", "смотритель"), Veterinarian("Мария Петровна", "ветеринар"),
         Personal("Сергей", "менеджер")]

for person in staff:
    zoo.add_personal(person)
