# Задача №3.
# Создайте класс Author и класс Book.
# Класс Book должен использовать композицию для включения автора в качестве объекта.

class Author():
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_book(self):
        print(f"{self.title} - {self.author.name} - {self.author.country}")

author = Author("Лев Толстой", "Россия")
book = Book("Война и мир", author)
# здесь использовали агрегацию, а не композицию!
book.get_info_book()