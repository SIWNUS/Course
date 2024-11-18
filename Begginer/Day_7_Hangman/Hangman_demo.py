import random;

word_list = ["aardvark", "buboon", "camel"]

# todo-1: Randomely choose a word from the word list and assign it to a variable called 'chosen_word' and print it.

# todo-2: Ask the user to guess a letter and assign it to a variable called 'guess'. Make huess lowercase.

# todo-3: Check if 'guess' is a letter from the 'chosen_word'. Print "Right" if yes and "wrong" if not.

chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Guess a Letter: ").lower()

for char in chosen_word:
    if guess == char:
        print("Right")
    else:
        print("Wrong")
