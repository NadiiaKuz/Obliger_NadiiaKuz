from datetime import date

"""Case 2 - Oppgave 7"""
class Car:
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km

    def print_car_information(self):
        """En metode i klassen er mer praktisk fordi den jobber direkte med objektets data
        og holder alt som er relatert til bilen samlet på ett sted"""

    def get_car_age(self):
        """Alder på en bil beregnes på produksjonsår, som er en attributter til klasse Car"""

    def rent_car_monthly_price(self):
        """Månedlig pris baseres på attributter 'price' til klasse Car,
        hvis vi skal ikke bruke eksterne variabler som RENT_NEW_CAR__FEE og RENT_CAR_PERCENTAGE"""

    def next_eu_control(self):
        """Neste eu kontrol baseres på attributer 'year' og 'month' til klasse Car"""

    def calculate_total_price(self):
        """Totalpris baseres på attributter 'price' til klasse Car,
        hvis vi skal ikke bruke eksterne variabler som AGE_FEE_MAP"""

    def is_new(self):
        """Også passer til klasse Car fordi det krever attributet 'new'"""

"""Jeg mener at disse metodene passer bedre for plassering inne i klassen, fordi det gjør koden mer objektorientert, 
ettersom de arbeider med data som allerede er lagret i klassens instans."""

car_register = {
    "toyotaBZ4X": {
         "brand": "Toyota",
         "model": "Corolla",
         "price": 96_000,
         "year": 2012,
         "month": 8,
         "new": False,
         "km": 163_000
    },
    "pugeot408": {
         "brand": "Pugeot",
         "model": "408",
         "price": 330_000,
         "year": 2019,
         "month": 1,
         "new": False,
         "km": 40_000
    },
    "audiRS3": {
         "brand": "Audi",
         "model": "RS3",
         "price": 473_000,
         "year": 2022,
         "month": 2,
         "new": True,
         "km": 0
    },
}
NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000

"""for at data fra tabellen blir gjenbrukbar"""
AGE_FEE_MAP = [
    (0, 3, 6681),
    (4, 11, 4034),
    (12, 29, 1729),
    (30, float('inf'), 0)
]

def print_car_information(car):
    """Case 2 - Oppgave 1"""
    if is_new(car):
        condition = 'New'
    else:
        condition = 'Used'
    print(f"Brand: {car['brand']} \nModel: {car['model']} \nPrice: {car['price']},- \nManufactured: {car['year']}-{car['month']} \nCondition: {condition} \nKm: {car['km']}")

def create_car(car_register, brand, model, price, year, month, new, km):
    """Case 2 - Oppgave 2"""
    car_key = f"{brand.lower()}{model}"
    car_value = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km": km
    }
    car_register[car_key] = car_value
    return car_value

def get_car_age(car):
    """Case 2 - Oppgave 3"""
    car_age = date.today().year - car['year']
    return car_age

def rent_car_monthly_price(car):
    """Case 2 - Oppgave 4"""
    monthly_price = (car['price'] * RENT_CAR_PERCENTAGE) / 12
    if is_new(car):
        return round((monthly_price + RENT_NEW_CAR__FEE), 2)
    else:
        return round(monthly_price, 2)

def next_eu_control(car):
    """Case 2 - Oppgave 5"""
    today_date = date.today()
    test_date = car['year']
    while date(test_date, car['month'], 1) < today_date:
        test_date += 2
    return date(test_date, car['month'], 1)

def calculate_total_price(car):
    """Case 2 - Oppgave 6"""
    car_age = get_car_age(car)
    price = car['price']
    if is_new(car):
        price += 10783
    else:
        for min_age, max_age, fee in AGE_FEE_MAP:
            if min_age <= car_age <= max_age:
                price += fee
    return price

def is_new(car):
    return car['new']

if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)

    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)
    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.")

    audi = car_register['audiRS3']
    print_car_information(audi)
    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")

    volvo = car_register['volvoV90']
    print_car_information(volvo)

    car = Car("Volvo", "V90", 850_000, 2021, 12, True, 0)
    car.print_car_information()

