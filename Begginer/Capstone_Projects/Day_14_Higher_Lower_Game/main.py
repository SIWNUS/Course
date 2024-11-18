#import logo and vs ascii arts from art.py
from art import logo, vs;
#import game data
from game_data import data;
import random;
import os;

def clear_screen():
    if os.system == 'nt':  #windows
        os.system('cls')
    else:  #Linux, MacOS and others
        os.system('clear')

def compare(num1, num2):
    if num1 >= num2:
        return True
    else:
        return False

def game():
    print(logo)

    dict_len = len(data)

    score = 0

    A = random.choice(data)
    ''' Because we need 2 elements to compare. Let's say dict_len == 1 at the last iteration.
        Then, the array would only have one element, the one 'A' contains. Then, 'B' will also have that same element.
        This is because random.choice(list) of a one element list will always return that element.
        This will make our if condition work infinitely. This can be solved easily.
        when dict_len == 1, stop the loop. Because that means our list has become a one element list.
    '''
    while dict_len != 1:
        B = random.choice(data)

        if A == B:
            B = random.choice(data)
        else:
            pass


        A_count = A['follower_count']
        B_count = B['follower_count']

        result = compare(A_count, B_count)

        if result == True:
            winner = 'A'
        else:
            winner = 'B'

        print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}\n")

        print(vs)

        print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if guess == winner:
            data.remove(A)
            dict_len = len(data)
            score +=  1
            print(f"You're right! Current score: {score} ")
            A = B
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            dict_len = 0

game()