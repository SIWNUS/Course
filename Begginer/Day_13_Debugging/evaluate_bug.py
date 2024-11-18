year = int(input("What is your year of birth? "))

if year > 1980 and year < 1994:
    print("You are millenial.")
elif year >= 1994: #The bug would be 'year > 1994'
    print("You are GenZ.")
else:
    print("You are too old.")