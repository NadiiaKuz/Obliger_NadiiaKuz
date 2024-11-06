# funksjon for å beregne summen av verdiene til kortene i hånden og endre verdien av esset hvis det trenges
def calculate_score(hand):
    score = 0
    ace_count = 0

    for card in hand:
        score += card.value
        if (card.rank == "Ace"):
            ace_count += 1

    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

def play_player (deck, player_hand):
    while True:
        print("----------------------------------------------------------------------------------")
        try: #sjekker at input 1 eller 2
            hit_or_stand_choice = int(input("Do you wish to hit or stand? \n 1 - Hit \n 2 - Stand \n Answer: "))
            if hit_or_stand_choice not in [1, 2]:
                print("Invalid choice. Please enter 1 for Hit or 2 for Stand.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")
            continue

        if hit_or_stand_choice == 1:
            player_hand.append(deck.deal_card())

            print(f"You have been dealt one card. Your hand now consists of the following cards:")
            for card in player_hand:
                print(f"- {card}")
            score = calculate_score(player_hand)
            print(f"The total value of your hand is now {score}")

            if score > 21: # spilleren taper, spillet er over
                print("----------------------------------------------------------------------------------")
                print(f"Bust! You lose")
                return False
        else:
            print("You chose to Stand")
            return True

def play_dealer (deck, dealer_hand):
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.deal_card())
    print("The dealer draws cards until their hand value is greater than 17. The dealers cards are the following:")
    for card in dealer_hand:
        print(f"- {card}")
    return dealer_hand

def get_winner (player_score, dealer_score, chips, bet_chips):
    if (dealer_score > 21 or player_score > dealer_score):
        print("You win!")
        chips += bet_chips * 2
    elif (dealer_score > player_score):
        print("Dealer win!")
    else:
        print("No one win")
        chips += bet_chips
    return chips

def play_again():
    while True:
        exit = input("Do you wish to play again? \n y - Yes \n n - No \n Answer: ").lower()
        if exit == "n" :
            print("See you next time!")
            return False
        elif exit == "y":
            return True
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No. ")