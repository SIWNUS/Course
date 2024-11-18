#todo: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#My solution

with open("Input/Names/invited_names.txt") as names:
    name = names.readlines()
    
with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.readlines()
    
    for person in name:
        person_name = person.strip()
        new_name = content[0].replace('[name]', person_name)
        with open(f"Output/ReadyToSend/letter_for_{person_name}.txt", "w") as file:
            file.write(new_name)
            file.writelines(content[1:])

#Teacher's solution

# with open("Input/Names/invited_names.txt") as names:
#     name = names.readlines()
    
# with open("Input/Letters/starting_letter.txt") as letter:
#     content = letter.read()
    
#     for person in name:
#         person_name = person.strip()
#         new_letter = content.replace('[name]', person_name)
#         with open(f"Output/ReadyToSend/letter_for_{person_name}.txt", "w") as file:
#             file.write(new_letter)


