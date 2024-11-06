import blackjack_game_logic as b

deck = b.get_new_deck()
chips = 7
while True:
    if (chips == 0):
        print("Sorry! You do not have any chips to bet")
        break

    if (len(deck.cards) < 15):
        deck = b.get_new_deck()
        print("Deck reshuffled due to low card count.")

    bet_chips = b.make_bet(chips)
    chips -= bet_chips
    print(f"You bet {bet_chips} chips. You have {chips} left after betting.")

    player_hand = [deck.deal_card(), deck.deal_card()]
    dealer_hand = [deck.deal_card(), deck.deal_card()]

    player_score = b.calculate_score(player_hand)
    dealer_score = b.calculate_score(dealer_hand)

    print("----------------------------------------------------------------------------------")
    print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[1]}, with a total value of {player_score}")
    print(f"The dealers visible card is a {dealer_hand[0]}")

    # Sjekker av Blackjack
    if (player_score == 21):
        print("Blackjack! You win!")
        chips += bet_chips * 2

    else:
        while True:
            print("----------------------------------------------------------------------------------")
            hit_or_stand_choice = b.get_hit_of_stand()
            overdraft = False

            if hit_or_stand_choice == 1:
                player_hand.append(deck.deal_card())

                print(f"You have been dealt one card. Your hand now consists of the following cards:")
                for card in player_hand:
                    print(f"- {card}")
                player_score = b.calculate_score(player_hand)
                print(f"The total value of your hand is now {player_score}")

                if (player_score > 21):
                    print("Bust! You lose!")
                    print(f"You have {chips} chips")
                    overdraft = True
                    break

            else:
                print("You chose to Stand")
                break

        if (not overdraft):
            # Hvis spilleren ikke har busted, spiller dealeren
            dealer_hand = b.play_dealer(deck, dealer_hand)

            player_score = b.calculate_score(player_hand)
            dealer_score = b.calculate_score(dealer_hand)

            print(f"The total value of the dealer hand is {dealer_score} compared to your hand's value {player_score}")
            print("----------------------------------------------------------------------------------")

            if (dealer_score > 21 or player_score > dealer_score):
                print("You win!")
                chips += bet_chips * 2
            elif (dealer_score > player_score):
                print("Dealer win!")
            else:
                print("No one win")
                chips += bet_chips

    print(f"You have {chips} chips now")
    print("----------------------------------------------------------------------------------")

    if (not b.play_again()):
        break