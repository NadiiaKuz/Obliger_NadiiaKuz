from cards import Deck
import blackjack_game_logic as b

deck = Deck()
deck.shuffle_deck()
chips = 7

while True:
    if (len(deck.cards) < 15):
        deck = Deck()
        deck.shuffle_deck()
        print("Deck reshuffled due to low card count.")

    while True:
        try:
            bet_chips = int(input(f"You currently have {chips} chips. How many do you bet?: "))
            if bet_chips <= 0 or bet_chips > chips:
                bet_chips = int(input("Invalid bet. Please enter a valid amount: "))
            else:
                break
        except ValueError:
            print("Invalid input!")

    print(f"You bet {bet_chips} chips out of your {chips} total.")
    chips -= bet_chips

    player_hand = [deck.deal_card(), deck.deal_card()]
    dealer_hand = [deck.deal_card(), deck.deal_card()]

    player_score = b.calculate_score(player_hand)
    dealer_score = b.calculate_score(dealer_hand)

    print("----------------------------------------------------------------------------------")

    print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[1]}, with a total value of {player_score}")
    print(f"The dealers visible card is a {dealer_hand[0]}")

    # Tester av Blackjack
    if (player_score == 21):
        print("Blackjack! You win!")
        chips += bet_chips * 2
    else:
        if (not b.play_player(deck, player_hand)): #
            # Spilleren tapte på grunn av "bust"
            print(f"You have {chips} chips")
            print("----------------------------------------------------------------------------------")
        else:
            # Hvis spilleren ikke har busted, spiller dealeren
            b.play_dealer(deck, dealer_hand)

            player_score = b.calculate_score(player_hand)
            dealer_score = b.calculate_score(dealer_hand)

            print(f"The total value of the dealer hand is {dealer_score} compared to your hand's value {player_score}")
            print("----------------------------------------------------------------------------------")
            chips = b.get_winner(player_score, dealer_score, chips, bet_chips)
            print(f"You have {chips} chips now")
            print("----------------------------------------------------------------------------------")

    if (not b.play_again()):
        break