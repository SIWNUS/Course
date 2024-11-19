# class Guest:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated(func):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             func(args[0])
#     return wrapper

# @is_authenticated
# def check(guest):
#     print(f"The guest of the day is: {guest.name}")

# new_guest = Guest("Suswin")
# check(new_guest)

# TODO: Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args):
        name = func.__name__
        value = func(*args)
        print(f"You called {name}{(args)}\nIt returned: {value}")
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)