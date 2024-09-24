print("Velkommen til pakkeliste!")
print("Hva vil du gjøre?")
packing_list = []

while True:

    print("1 - legge til noe, 2 - slette noe, 3 - se hele listen, 4 - avslutte programmet")

    command_number = input("Skriv nummeret på kommandoen du vil utføre: ")

    if (command_number == '1'):
        add_item = input("Hvilket element vil du legge til?: ").lower()
        packing_list.append(add_item)
    elif (command_number == '2'):
        delete_item = input("Hvilket element vil du slette?: ").lower()
        if (delete_item not in packing_list):
            print("Dette elementet finnes ikke på listen")
        else:
            packing_list.remove(delete_item)
    elif (command_number == '3'):
        print(f"Pakkelisten din inneholder: {packing_list}")
    elif (command_number == '4'):
        print("Ha den god reise!")
        break
    else:
        print("Det finnes ingen kommando med dette nummeret")