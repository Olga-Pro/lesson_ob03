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

# для сохранения в файл и загрузки обратно через сериализацию
import pickle

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
        return "питается семенами и насекомыми"

class Mammal(Animal):
    def eat(self):
        return "в детстве питается молоком"

class Reptile(Animal):
    def eat(self):
        return "питается насекомыми"
class Turtle(Reptile):
    def make_sound(self):
        return "молчит"

    def eat(self):
        return "питается растительной пищей"

    def get_type(self):
        return "Черепаха"

class Serpent(Reptile):
    def make_sound(self):
        return "шшш"

    def eat(self):
        return "питается мелкими грызунами"

    def get_type(self):
        return "Змея"

class Tiger(Mammal):
    def make_sound(self):
        return "ррр"

    def eat(self):
        return "питается мясом"

    def get_type(self):
        return "Тигр"

class Goal(Mammal):
    def make_sound(self):
        return "бее"

    def eat(self):
        return "питается травой"

    def get_type(self):
        return "Коза"

class Elephant(Mammal):
    def make_sound(self):
        return "уууу"

    def eat(self):
        return "питается растительной пищей"

    def get_type(self):
        return "Слон"

class Peacock(Bird):
    def make_sound(self):
        return "очень неприятно кричит"

    def get_type(self):
        return "Павлин"

class Cuckoo(Bird):
    def make_sound(self):
        return "ку-ку"

    def get_type(self):
        return "Кукушка"

class Personal():
    def __init__(self, name, position=""):
        self.name = name
        self.position = position

class ZooKeeper(Personal):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.position = "смотритель"
    def feed_animal(self):
        return "кормит животных"

class Veterinarian(Personal):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.position = "ветеринар"
    def heal_animal(self):
        return "лечит животных"

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []
    def add_personal(self, person):
        self.staff.append(person)

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_animals(self):
        print("\nСостав зоопарка:")
        for animal in self.animals:
            print(f"{animal.get_type()} по имени {animal.name} возраст {animal.age}")

    def print_staff(self):
        print("\nСотрудники зоопарка:")
        for person in self.staff:
            print(f"{person.name} {person.position} ")

#-------------------------------------------------------------------------------
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
def animal_sound(list_animals):
    for animal in list_animals:
        print(f"{animal.get_type()} - звук: {animal.make_sound()} - {animal.eat()}")


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

zoo.print_animals()
zoo.print_staff()

print("\nСохраняем в файл")
# Сериализация объекта zoo в файл
with open('zoo.pkl', 'wb') as output:
    pickle.dump(zoo, output, pickle.HIGHEST_PROTOCOL)

print("Новый пустой зоопарк")
zoo2 = Zoo()
zoo2.print_animals()
zoo2.print_staff()

print("\nВосстанавливам из файла")
# Десериализация объекта из файла
with open('zoo.pkl', 'rb') as input_file:
    zoo2 = pickle.load(input_file)

zoo2.print_animals()
zoo2.print_staff()


