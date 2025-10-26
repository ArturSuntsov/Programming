from datetime import datetime
from abc import ABC, abstractmethod


class Book:
    """
    Базовый класс для книг
    """
    def __init__(self, title: str, author: str, year: int):
        """
        шаблон для создания книги
        :param title: str
        :param author: str
        :param year: int
        """
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        """
        Возвращает строку с информацией о книге
        :return: str
        """
        return f"{self.title}, {self.author}, {self.year}"
    
    class Printable(ABC):
        """
        Абстрактный вложенный класс для печатаемых объектов
        """
        @abstractmethod
        def print_info(self):
            """
            Абстрактный метод для вывода информации
            :return: None
            """
            pass


class Ebook(Book):
    """
    Класс для электронных книг
    """
    def __init__(self, title: str, author: str, year: int, format: str):
        """
        Шаблон для создания электронной книги
        :param title: str
        :param author: str
        :param year: int
        :param format: str
        """
        super().__init__(title, author, year)
        self.format = format

    def info(self) -> str:
        """
        Возвращает расширенную информацию об электронной книге
        :return: str
        """
        return f"{self.title}, {self.author}, {self.year}, {self.format}"

    def __str__(self):
        """
        Возвращает строковое представление электронной книги
        :return: str
        """
        return self.info()
    
    def __eq__(self, other):
        """
        Сравнивает две электронные книги по названию
        :param other: Ebook
        :return: bool
        """
        return isinstance(other, Ebook) and self.title == other.title
    
    @property
    def age(self):
        """
        Возвращает возраст книги в годах
        :return: int
        """
        return datetime.now().year - self.year
    
    @age.setter
    def age(self, value):
        """
        Устанавливает год издания на основе возраста
        :param value: int
        :return: None
        """
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        """
        Создаёт экземпляр Ebook 
        :param data: str
        :return: Ebook
        """
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
