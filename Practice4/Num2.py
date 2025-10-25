class Car:


    def __init__(self, brand):
        self.brand = brand

    def review(self):
        return f'{self.brand} - Дефолтное авто'
    
    def calculate_price(self):
        return 'Никак не оценивается'
    
class SUV(Car):


    def __init__(self, brand, size):
        super().__init__(brand)
        self.size = size

    def review(self):
        return f'{self.brand} - Это мощный внедоржник!'
    
    def calculate_price(self):
        return self.size * 100000
    
class Sportcar(Car):


    def __init__(self, brand, horse_power):
        super().__init__(brand)
        self.horse_power = horse_power

    def review(self):
        return f'{self.brand} - Это быстрый спорткар!'
    
    def calculate_price(self):
        return self.horse_power * 30000
    
class Electriccar(Car):


    def __init__(self, brand, reserve_km):
        super().__init__(brand)
        self.reserve_km = reserve_km

    def review(self):
        return f'{self.brand} - Это технологичный электрокар!'
    
    def calculate_price(self):
        return self.reserve_km * 5000
    
suv = SUV('Jeep', 43)
sportcar = Sportcar('Ferrari', 700)
electriccar = Electriccar('Tesla', 1000)

print(suv.review())
print(sportcar.review())
print(electriccar.review())
