import random;
import Hangman_art;
import Hangman_words;

print(Hangman_art.logo)

lives = 6

chosen_word = random.choice(Hangman_words.word_list)

placeholder = ""

for char in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False

display_list = []

while not game_over:

    print(f"*****************You have {lives} chances left to try*****************")

    guess = input("Guess a Letter: ").lower()

    if guess in display_list:
        print(f"You have already guessed {guess}")

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

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, but it is not a letter in the given word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"The correct word is {chosen_word}")
            print("*****************You Lose*****************")

    if "_" not in display:
        game_over = True
        print("*****************You Win*****************")

    print(Hangman_art.stages[lives])