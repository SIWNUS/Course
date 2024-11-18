from art import logo;
import random;

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

def compare(num1, num2):
    if num1 < num2:
        return "Too low."
    else:
        return "Too high."
    
def set_difficulty(dif):
    if dif == 'easy':
        return 10
    else:
        return 5

def guess_the_number():
    global number

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = set_difficulty(difficulty)

    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess != number:
            result = compare(guess, number)
            attempts -= 1
            print(result)
            if attempts == 0:
                print("You are out of turns. You lost.")
            else:
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {guess}.")
            attempts = 0
                
guess_the_number()