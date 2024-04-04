import pickle

# Пример определения классов
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.species} named {self.name}"

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        animals_list = "\n".join([str(animal) for animal in self.animals])
        return f"Zoo: {self.name}\nAnimals:\n{animals_list}"

# Создание объектов
zoo = Zoo("My Amazing Zoo")
zoo.add_animal(Animal("Leo", "Lion"))
zoo.add_animal(Animal("Stripes", "Tiger"))

# Сериализация объекта zoo в файл
with open('zoo.pkl', 'wb') as output:
    pickle.dump(zoo, output, pickle.HIGHEST_PROTOCOL)

# Десериализация объекта из файла
with open('zoo.pkl', 'rb') as input_file:
    loaded_zoo = pickle.load(input_file)
    print(loaded_zoo)