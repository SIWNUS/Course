import random;

word_list = ["aardvark", "buboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""

i = 0       #"i" is length of the 'chosen_word'.

for char in chosen_word:
    placeholder += "_"
    i += 1

print(placeholder)

# todo-1: Use a while loop to let the user guess again.

game_over = False

display_list = []

while not game_over:

    guess = input("Guess a Letter: ").lower()

    display = ""

# todo-2: Change the for loop so that we can keep the previous correct guess for the next loop.

    for char in chosen_word:
        if guess == char:
            display += guess
            display_list += guess
        elif char in display_list:
            display += char
        else:
            display += "_"

    print(display)

    i -= 1

    if "_" not in display:
        game_over = True
        print("You Win.")
    elif i == 0:
        game_over = True
        print("YOu Lose.")

