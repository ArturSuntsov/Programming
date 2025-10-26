class Employee:
    """
    Базовый класс для сотрудников
    """
    main_payment = 100000

    def __init__(self, name):
        """
        шаблон для создания сотрудника
        :param name: str
        """
        self.name = name
          
    def calculate_payment(self):
        """
        Рассчитывает зарплату
        :return: int
        """
        return self.main_payment


class Manager(Employee):
    """
    Класс для менеджеров
    """
    def __init__(self, name, team_size):
        """
        шаблон для создания менеджера
        :param name: str
        :param team_size: int
        """
        super().__init__(name)
        self.team_size = team_size

    def calculate_payment(self):
        """
        Рассчитывает зарплату с надбавкой за размер команды
        :return: int
        """
        return self.main_payment + self.team_size * 5000


class Developer(Employee):
    """
    Класс для разработчиков
    """
    def __init__(self, name, frameworks):
        """
        шаблон для создания разработчика
        :param name: str
        :param frameworks: int
        """
        super().__init__(name)
        self.frameworks = frameworks

    def calculate_payment(self):
        """
        Рассчитывает зарплату с надбавкой за количество фреймворков
        :return: int
        """
        return self.main_payment + self.frameworks * 8000


manager = Manager('Алиса', 10)
developer = Developer('Иван', 14)

print(manager.calculate_payment())
print(developer.calculate_payment())
