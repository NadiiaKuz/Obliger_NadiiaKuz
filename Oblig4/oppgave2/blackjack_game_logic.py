from cards import Deck

def get_new_deck():
    deck = Deck()
    deck.shuffle_deck()
    return deck

# funksjon for å sjekke spillerens innsats
def make_bet(chips):
    while True:
        try:
            bet_chips = int(input(f"You currently have {chips} chips. How many do you bet?: "))
            if bet_chips <= 0 or bet_chips > chips:
                print("Invalid bet. Please enter a valid amount: ")
            else:
                return bet_chips
        except ValueError:
            print("Invalid input!")

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

def get_hit_of_stand():
    while True:
        try:  # sjekker at input 1 eller 2
            hit_or_stand_choice = int(input("Do you wish to hit or stand? \n 1 - Hit \n 2 - Stand \n Answer: "))
            if hit_or_stand_choice not in [1, 2]:
                print("Invalid choice. Please enter 1 for Hit or 2 for Stand.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")
            continue
        return hit_or_stand_choice

def play_dealer (deck, dealer_hand):
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.deal_card())
    print("The dealer draws cards until their hand value is greater than 17. The dealers cards are the following:")
    for card in dealer_hand:
        print(f"- {card}")
    return dealer_hand

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