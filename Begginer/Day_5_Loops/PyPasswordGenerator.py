import random

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symblos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to pyPassowrd Generator!")
nl = int(input("How many letters?"))
nn = int(input("How many numbers?"))
ns = int(input("How many symblos?"))

#Easy level
password = ""

for char in range(1, nl+1):
    rc = random.choice(letters)
    password += rc

for num in range(1, nn+1):
    rn = random.choice(numbers)
    password += rn

for sym in range(1, ns+1):
    rs = random.choice(symblos)
    password += rs

print(password)

#Hard Level
password_list = []

for char in range(1, nl+1):
    rc = random.choice(letters)
    password_list += rc

for num in range(1, nn+1):
    rn = random.choice(numbers)
    password_list += rn

for sym in range(1, ns+1):
    rs = random.choice(symblos)
    password_list += rs

print(password_list)
random.shuffle(password_list)
print(password_list)

random_password = ""

for rp in password_list:
    random_password += rp

print(random_password)
