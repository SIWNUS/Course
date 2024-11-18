from art import logo;
import os;

def clear_screen():
    if os.system == "nt":
        os.system("cls")
    else:
        os.system("clear")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():

    print(logo)

    calc = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    a = int(input("What is your first number? "))

    end = False

    while not end:
        operator = input("What is your operator?\n'+'\n'-'\n'*;\n'/'\n")
        b = int(input("What is your next number? "))
        result = 0
        if operator == "+" or operator == "-" or operator == "*" or operator == "/": 
            for key in calc:
                if operator == key:
                    key = calc[key]
                    result += key(a, b)
                    print(f"The result is: {result}")

        print(f"Type 'y' to continue with the result {result} or type 'n' to terminate:\n")
        cont = input().lower()

        if cont == "n" or cont == "no":
            print(f"The final reslut is: {result}")
            end = True
            clear_screen()
            calculator()
        elif cont == "y" or cont == "yes":
            a = result
        else:
            print("Respone unacceptable. Try again.\n")
            print(f"Type 'y' to continue with the result {result} or type 'n' to terminate:\n")
            cont = input().lower()
            a = result
            operator = input("What is your operator?\n'+'\n'-'\n'*;\n'/'\n")

calculator()
            