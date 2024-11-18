def greet(name, location):
    print(f"Hello, {name}!")
    print(f"I heard you are from {location}.")
    print("This is a demo function call with more than one parameters.")

greet("Bennett", "Mondstadt")

# These are called positional arguments.

greet(name="Bennett", location="Mondstadt")

# These are keyword arguments