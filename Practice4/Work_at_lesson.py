from datetime import datetime
from abc import ABC, abstractmethod

class Book:

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        return f"{self.title}, {self.author}, {self.year}"
    
    class Printable(ABC):
        @abstractmethod
        def print_info(self):
            pass
    
class Ebook(Book):

    def __init__(self, title: str, author: str, year: int, format: str):
        super().__init__(title, author, year)
        self.format = format

    def info(self) -> str:
        return f"{self.title}, {self.author}, {self.year}, {self.format}"

    def __str__(self):
        return self.info()
    
    def __eq__(self, other):
        return isinstance(other, Ebook) and self.title == other.title
    
    @property
    def age(self):
        return datetime.now().year - self.year
    
    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        title, author, year, format = data.split(";")
        return cls(title, author, int(year), format)

book1 = Ebook("Война и мир", "Лев Толстой", 1864, "PDF")
print(book1)

book2 = Ebook("Eugene Onegin", "Alexander Pushkin", 1884, "PDF")
print(book2.info())

print(book1 == book2)

book3 = Ebook("Преступление и наказание", "Федор Достоевский", 1864, "PDF")
print(book3.age)

book4 = Ebook.from_string("1984;Оруэлл;1949;PDF")
print(book4)
