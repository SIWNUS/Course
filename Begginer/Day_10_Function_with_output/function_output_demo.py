def format_name(f_name, l_name):
    fname = f_name.title()
    lname = l_name.title()
    return f"{fname} {lname}"

fname = input("What is your first name? ")
lname = input("What is your last name? ")

formatted_name = format_name(fname, lname)
print(formatted_name)