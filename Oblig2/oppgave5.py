from random import randrange

number_of_players = int(input("Skriv antall spillere (skriv et tall!): "))

for player in range(1, number_of_players + 1):
    throw_1 = randrange(61)
    throw_2 = randrange(61)
    throw_3 = randrange(61)
    sum_of_throws = throw_1 + throw_2 + throw_3
    print(f"Spiller {player}. Første kast: {throw_1} poeng. Andre kast: {throw_2} poeng. Tredje kast: {throw_3} poeng. Score: {sum_of_throws}")