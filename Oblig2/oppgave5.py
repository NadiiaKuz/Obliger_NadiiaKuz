from random import randrange

number_of_players = int(input("Skriv antall spillere (skriv et tall!): "))

players = 1

while players <= number_of_players:
    throw_1 = randrange(61)
    throw_2 = randrange(61)
    throw_3 = randrange(61)
    sum_of_throws = throw_1 + throw_2 + throw_3
    print(f"Første kast: {throw_1} poeng. Andre kast: {throw_2} poeng. Tredje kast: {throw_3} poeng. Score: {sum_of_throws}")
    players += 1