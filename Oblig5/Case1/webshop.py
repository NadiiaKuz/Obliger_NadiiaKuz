#------------------------------------------
#Oppgaver
#------------------------------------------
"""Case 1 - Oppgave 1"""
def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    print(f"Name: {ware['name']} \nPrice: {ware['price']},- \nNumber in stock: {ware['number_in_stock']} \nDescription: {ware['description']}\n")

"""Case 1 - Oppgave 2"""
def calculate_average_ware_rating(ware):
    '''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    try:
        ratings = ware['ratings']
        result = sum(ratings) / len(ratings)
        return round(result, 1)
    except ZeroDivisionError:
        print("Det finnes ingen rating")

"""Case 1 - Oppgave 3"""
def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    wares_in_stock = {}
    for ware_key, ware_value in all_wares.items():
        if ware_value['number_in_stock'] > 0:
            wares_in_stock[ware_key] = ware_value
    return wares_in_stock

"""Case 1 - Oppgave 4"""
def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall av en gitt vare finnes på lager.'''
    if ware['number_in_stock'] >= number_of_ware:
        return True
    else:
        return False

"""Case 1 - Oppgave 5"""
def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert handlevogn.'''
    if is_number_of_ware_in_stock(ware, number_of_ware):
        shopping_cart[ware_key] = number_of_ware
        print(f"{number_of_ware} instance(s) of {ware['name']} were added to the shopping cart.")
    elif ware['number_in_stock'] > 0:
        available_in_stock = ware['number_in_stock']
        shopping_cart[ware_key] = available_in_stock
        print(f"Only {available_in_stock} instance(s) of {ware['name']} were in stock. These were added to the shopping cart.")
    else:
        print(f"{ware['name']} is not in stock and could not be added to the shopping cart.")
    return shopping_cart

"""Case 1 - Oppgave 6"""
def calculate_shopping_cart_price(shopping_cart, all_wares, tax=25):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''
    total_price = 0
    for ware_key, ware_value in shopping_cart.items():
        if ware_key in all_wares:
            total_price += all_wares[ware_key]["price"] * ware_value
    price_with_tax = total_price + total_price * tax / 100
    return round(price_with_tax, 1)

def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt lommebok for å kjøpe en handlevogn.'''

def buy_shopping_cart():
    '''Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.'''
    #------------------------------------------
    # Predefinerte funksjoner
    #------------------------------------------

def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False

def clear_shopping_cart(shopping_cart):
    '''Tømmer en handlevogn.'''
    shopping_cart.clear()
