
class Car:
    # konstruktor method for å initialisere objekter
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # method for å beskrive bilen
    def get_info(self):
        return f"Bil {self.brand} {self.model} produsert i {self.year}"


#Oppreter av et objekt av klasse Car
my_car = Car("Toyota", "Camry", 2015)
print(my_car.get_info())