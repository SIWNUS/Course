from menu import MENU, resources
import os

money = 0

def clear_screen():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def resources_list():
    global money
    resources['money'] = money
    for key in resources:
        print(f"{key}: {resources[key]}")
    del resources['money']
        
def payment(price):
    print("Please insert coins.")
    quarter = int(input("How many quarters (25 cents)? $"))
    dimes = int(input("How many dimes (10 cents)? $"))
    nickels = int(input("How many nickels (5 cents)? $"))
    pennies = int(input("How many pennies (1 cent)? $"))

    
    pay = (quarter * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if pay == price:
        return True
    elif pay > price:
        return pay - price
    else:
        return False

def make_coffee(choice):
    for item in resources:
        if resources[item] < choice[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def resource_deduct(choice, paid):
    if paid != False:
        for ingredient in MENU[choice]['ingredients']:
            resources[ingredient] -= MENU[choice]['ingredients'][ingredient]

def coffee_machine():

    working = True

    while working:

        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_choice == 'report':
            resources_list()

        elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
            drink = MENU[user_choice]
            coffee = make_coffee(drink['ingredients'])

            if coffee == True:
                price = drink['cost']
                print(f"The cost of {user_choice} is ${price}")
                user_paid = payment(price=price)
                resource_deduct(user_choice, user_paid)

                if user_paid == True:
                    print(f"Here is your ${user_choice}. Enjoy!")
                    money += price
                elif user_paid == False:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    user_paid = round(user_paid, 2)
                    print(f"Here is ${user_paid} in change.")
                    print(f"Here is your {user_choice}. Enjoy!")
                    money += price

        elif user_choice == 'off':
            clear_screen()
            working = False

        else:
            print("invalid response! Try again!")

coffee_machine()