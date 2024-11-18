from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

def clear_screen():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

def coffee_machine():

    end = False

    while not end:

        user_choice = input(f"What would you like? {menu.get_items()}: ").lower()

        if user_choice == 'off':
            clear_screen()
            end = True
        elif user_choice == 'report':
            coffee_maker.report()
            money.report()
        elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
            drink = menu.find_drink(user_choice)
            take_order = coffee_maker.is_resource_sufficient(drink=drink)
            if take_order == True:
                price = drink.cost
                print(f"The price of {drink.name} is: ${price}")
                payment = money.make_payment(price)
                if payment == True:
                    coffee_maker.make_coffee(drink)
        else:
            print("Invalid input. Try again!")

coffee_machine()