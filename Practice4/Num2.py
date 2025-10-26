class Car:
    """
    Базовый класс для автомобилей
    """
    def __init__(self, brand):
        """
        шаблон для создания автомобиля
        :param brand: str
        """
        self.brand = brand

    def review(self):
        """
        Возвращает общее описание автомобиля
        :return: str
        """
        return f'{self.brand} - Дефолтное авто'
    
    def calculate_price(self):
        """
        Рассчитывает цену автомобиля
        :return: str
        """
        return 'Никак не оценивается'


class SUV(Car):
    """
    Класс для внедорожников
    """
    def __init__(self, brand, size):
        """
        шаблон для создания внедорожника
        :param brand: str
        :param size: int
        """
        super().__init__(brand)
        self.size = size

    def review(self):
        """
        Возвращает описание внедорожника
        :return: str
        """
        return f'{self.brand} - Это мощный внедоржник!'
    
    def calculate_price(self):
        """
        Рассчитывает цену внедорожжника
        :return: int
        """
        return self.size * 100000


class Sportcar(Car):
    """
    Класс для спорткаров
    """
    def __init__(self, brand, horse_power):
        """
        шаблон для создания спорткара
        :param brand: str
        :param horse_power: int
        """
        super().__init__(brand)
        self.horse_power = horse_power

    def review(self):
        """
        Возвращает описание спорткара
        :return: str
        """
        return f'{self.brand} - Это быстрый спорткар!'
    
    def calculate_price(self):
        """
        Рассчитывает цену спорткара
        :return: int
        """
        return self.horse_power * 30000


class Electriccar(Car):
    """
    Класс для электромобилей
    """
    def __init__(self, brand, reserve_km):
        """
        шаблон для создания электрокара
        :param brand: str
        :param reserve_km: int
        """
        super().__init__(brand)
        self.reserve_km = reserve_km

    def review(self):
        """
        Возвращает описание электромобиля
        :return: str
        """
        return f'{self.brand} - Это технологичный электрокар!'
    
    def calculate_price(self):
        """
        Рассчитывает цену электромобиля
        :return: int
        """
        return self.reserve_km * 5000


suv = SUV('Jeep', 43)
sportcar = Sportcar('Ferrari', 700)
electriccar = Electriccar('Tesla', 1000)

print(suv.review())
print(sportcar.review())
print(electriccar.review())
