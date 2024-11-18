from art import logo;
import os;

print(logo)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

bidders = {}

auction_end = False

while not auction_end:

    print("\n")
    print("Welccome to the auction programme.\n")
    print("Please Fill the details below:\n")

    name = input("Enter your name: ")
    bid = input("Enter your bid: $")

    print("Are there more bidders? Type 'Yes' or 'No'...")

    cont = input().lower()

    if cont == "yes":
        bidders[name] = bid
        clear_screen()
    else:
        bidders[name] = bid
        highest_bid = 0
        win = []
        for key in bidders:
            key_bid = int(bidders[key])
            if key_bid > highest_bid:
                highest_bid = key_bid
            
        winning_bid = str(highest_bid)

        for keys in bidders:
            if bidders[keys] == winning_bid:
                win.append(keys)
                win.append(bidders[keys])

        clear_screen()

        print(f"The winner of this auction is {win[0]} with the bid of ${win[1]}")

        auction_end = True
