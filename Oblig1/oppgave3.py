while True:
    try:
        number1 = float(input("Skriv første tall: ")) #gir brukeren mulighet til å skrive inn tall og sjekker om input er et tall
        number2 = float(input("Skriv andre tall: "))
    except ValueError:
        print("Du må skrive bare et tall!") #håndterer feilen hvis input ikke er et tall
        continue #starter på nytt hvis input ikke er et tall


    operator = input("Skriv tegnet på operasjonen (for eksempel: '*', '/', '+', '-', '%', '**', '//'): ")

    if (operator == '*'):
        answer = number1 * number2
        print(f"Svaret er {answer}")
    elif (operator == '/'):
        if (number2 == 0): #sjekker at brukeren prøver å dele på 0
            print("Du kan ikke dele på 0")
        else:
            answer = number1 / number2
            print(f"Svaret er {answer}")
    elif (operator == '+'):
        answer = number1 + number2
        print(f"Svaret er {answer}")
    elif (operator == '-'):
        answer = number1 - number2
        print(f"Svaret er {answer}")
    elif (operator == '%'):
        answer = number1 % number2
        print(f"Svaret er {answer}")
    elif (operator == '**'):
        answer = number1 ** number2
        print(f"Svaret er {answer}")
    elif (operator == '//'):
        if (number2 == 0):
            print("Du kan ikke dele på 0")
        else:
            answer = number1 // number2
            print(f"Svaret er {answer}")
    else: #sjekker at brukeren har skrevet riktig tegn
        print("Dette operasjonstegn er ikke tillat")