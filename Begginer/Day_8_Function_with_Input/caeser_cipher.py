from caeser_art import logo;

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_text, shift_amount, encode_or_decode):
        
        out_text = ""

        if encode_or_decode == "decode":
            shift_amount *= -1

        for letter in original_text:
            if letter in alphabet:
                new_index = alphabet.index(letter) + shift_amount
                new_index %= len(alphabet)
                out_text += alphabet[new_index]
            else:
                out_text += letter

        print(f"Here is the {encode_or_decode}d result: {out_text}")

crypt = True

while crypt is True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    
    caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    pref = input("Type 'Yes' if you want to go again. Oyherwise type 'No':\n").lower()

    if pref == "yes":
        pass
    elif pref == "no":
        crypt = False
        print("Goodbye!")
    else:
        print("Invalid Input!!!")
        crypt = False
        
