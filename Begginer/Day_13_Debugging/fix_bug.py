#bugged code
# age = int(input("What is your age? "))

# if age > 18:
#     print(f"my age is {age}")

#corrected code
#using try-except block to catch the error
try:
    age = int(input("What is your age? "))
except ValueError:
    print("Invalid response. Please give a numerical response like 15.")
    age = int(input("What is your age? "))

if age > 18:
    print(f"my age is {age}")