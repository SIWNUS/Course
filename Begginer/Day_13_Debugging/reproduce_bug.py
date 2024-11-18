from random import randint;

dice_images = [1, 2, 3, 4, 5, 6]

#bugged code
dice_num = randint(a=1, b=6)
''' Here, you could use try-except block to catch the error instead of trying out a lot of things.
    Also to note, with our bugged code, we can never print 1 from dice_images because dice_num which
    acts as our index can never become 0. So, changing the code is easy.
    As long as randint(a=0, b=5), then our code will work. Our correct code down will show it.'''
try:
    print(dice_images[dice_num])
    print("\n")
except IndexError:
    print("Indexerror: list index out of range.")
    print(f"{dice_num} is not in index.\n")

#correct code
dice_num = randint(a=0, b=5)
print(f"dice_num is: {dice_num}. This is our index.")
print(f"the dice image would be: {dice_images[dice_num]}")