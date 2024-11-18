from art import logo;
import random;
import os;

def clear_screen():
    if os.system == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ace(card, score):
    if card == 11:
        if score > 10:
            return card - 10
        else:
            return card
    else:
        return card
    
def check_win(score1, score2):
    if score2 == 21:
        return True
    elif score2 < 21:
        if score2 > score1:
            return True
        elif score1 > score2:
            return False
        else:
            return "Darw!"
    else:
        return False
    
def blackjack_logic():

    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player = random.choices(cards, k=2)
    dealer = random.choices(cards, k=2)

    player_score = player[0] + player[1]
    dealer_score = dealer[0] + dealer[1]

    next_hand = False

    while not next_hand:
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {dealer[0]}")

        if player_score == 21:
            print("Blackjack! You Win!")
            next_hand = True
        elif player_score < 21:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == 'y':
                new_player_card = random.choice(cards)
                new_player_card = ace(card=new_player_card, score=player_score)
                new_dealer_card = random.choice(cards)
                new_dealer_card = ace(card=new_dealer_card, score=dealer_score)
                player.append(new_player_card)
                player_score += new_player_card
                dealer.append(new_dealer_card)
                dealer_score += new_dealer_card
            elif choice == 'n':
                while dealer_score != 0 and dealer_score < 17:
                    new_dealer_card = random.choice(cards)
                    new_dealer_card = ace(card=new_dealer_card, score=dealer_score)
                    dealer.append(new_dealer_card)
                    dealer_score += new_dealer_card
                    
                next_hand = True
                print(f"Your final hand: {player}, final score: {player_score}")
                print(f"Computer's final hand: {dealer}, final score: {dealer_score}")
                check = check_win(player_score, dealer_score)
                if check == True:
                    print("You Lose!")
                elif check == False:
                    print("You Win!")
                else:
                    print(check)
            else:
                print("invalid response. Try again.\n")
        else:
            next_hand = True
            print("You Lose!")

def blackjack():
    new_game = False

    while not new_game:
        cont = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
        if cont == 'y':
            clear_screen()
            blackjack_logic()
        elif cont == "n":
            new_game = True
            clear_screen()
            print("Bye! Have a nice day!")
        else:
            print("Invalid response. Try again.")

blackjack()