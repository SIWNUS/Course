import random;
import Hangman_art;

print(Hangman_art.logo)

word_list = ["aardvark", "buboon", "camel"]

# todo-1: Create a variable called 'lives' to keep track of the chances left. Set it to 6 initially.

lives = 6

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""

for char in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False

display_list = []

while not game_over:

    guess = input("Guess a Letter: ").lower()

    display = ""

    for char in chosen_word:
        if guess == char:
            display += guess
            display_list += guess
        elif char in display_list:
            display += char
        else:
            display += "_"

    print(display)

    # todo-2: if guess is not a letter in chosen_word, reduce lives by one; if lives = 0, then game over and print you lose.

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose.")

    if "_" not in display:
        game_over = True
        print("You Win.")

    # todo-3: print the ASCII art corresponding to the no.of.lives from the list stages.

    print(Hangman_art.stages[lives])
    print(f"You have {lives} chances left to try.")