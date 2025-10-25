class Employee:
    main_payment = 100000

    def __init__(self, name):
        self.name = name
          
    def calculate_payment(self):
        return self.main_payment

class Manager(Employee):


    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def calculate_payment(self):
        return self.main_payment + self.team_size * 5000
    
class Developer(Employee):
    

    def __init__(self, name, frameworks):
        super().__init__(name)
        self.frameworks = frameworks

    def calculate_payment(self):
        return self.main_payment + self.frameworks * 8000
    
manager = Manager('Алиса', 10)
developer = Developer('Иван', 14)

print(manager.calculate_payment())
print(developer.calculate_payment())
