import pandas as pd # type: ignore

#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()} 

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetics():
    user_input = input("What is the word? ").upper()

    try:
        nato_word = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:
        print(nato_word)

generate_phonetics()
