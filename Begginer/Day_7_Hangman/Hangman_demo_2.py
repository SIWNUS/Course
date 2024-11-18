import random;

word_list = ["aardvark", "buboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

# todo-1: Create a "placeholder" with the same number of blanks as there are letters in the 'chosen_word'.

placeholder = ""

for char in chosen_word:
    placeholder += "_"

print(placeholder)

guess = input("Guess a Letter: ").lower()

# todo-2: Create a "display" that puts the guess letter in the right blanks.

display = ""

for char in chosen_word:
    if guess == char:
        display += guess
    else:
        display += "_"

print(display)