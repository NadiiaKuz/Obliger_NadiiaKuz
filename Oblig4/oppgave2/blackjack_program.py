while True:
    chips = 7
    player_score = 0
    dealer_score = 0
    bet_chips = int(input("You currently have 7 chips. How many do you bet?: "))
    chips = chips - bet_chips
    print(f"You bet {bet_chips} out of your 7 total.")

    #get_random_card to ganger, player_score = randon_card + randon_card
    print(f"The cards have been dealt. You have a Eight of clubs and a Three of hearts, with a total value of {player_score}")

    #get_random_card to ganger, dealer_score = randon_card + randon_card. Men viser vi bare en cort
    print(f"The dealers visible card is a Five of hearts, with a value of {dealer_score}")

    hit_or_stand_choise = int(input("Do you wish to hit or stand? \n 1 - Hit \n 2 - Stand \n Answer: "))
    if hit_or_stand_choise == 1:
        #get_random_card, player_score += random_card
        print("You chose to Hit")
        print(f"You have been dealt one card. Your hand now consists of the following cards: \n "
              f"The total value of your hand is now {player_score}, and the dealers' is 5")
    else:
        print("You chose to Stand")

