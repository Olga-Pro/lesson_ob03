import json

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def make_sound(self):
        pass

    def to_dict(self):
        return {"species": self.species, "name": self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
class Lion(Animal):
    def __init__(self, name):
        super().__init__("Lion", name)
    def make_sound(self):
        return "ppp"

class Personal:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def to_dict(self):
        return {"name": self.name, "position": self.position}

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def add_staff(self, person):
        if isinstance(person, Personal):
            self.staff.append(person)

    def save_to_file(self, filename):
        data = {
            "animals": [animal.to_dict() for animal in self.animals],
            "staff": [person.to_dict() for person in self.staff]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self.animals = [Animal.from_dict(animal) for animal in data["animals"]]
            self.staff = [Personal.from_dict(person) for person in data["staff"]]

# Пример использования
zoo = Zoo()

# Добавляем животных и сотрудников
zoo.add_animal(Animal("Tiger", "Basrik"))
zoo.add_animal(Lion( "Leo"))

zoo.add_staff(Personal("John", "Keeper"))
zoo.add_staff(Personal("Mark", "Manager"))

# Сохраняем в файл
zoo.save_to_file("zoo_data.json")

# Создаем новый экземпляр зоопарка
new_zoo = Zoo()

# Загружаем данные из файла
new_zoo.load_from_file("zoo_data.json")

# Проверяем, что данные загрузились корректно
for animal in new_zoo.animals:
    print(f"Animal: {animal.name}, Species: {animal.species}")
for person in new_zoo.staff:
    print(f"Name: {person.name}, Position: {person.position}")