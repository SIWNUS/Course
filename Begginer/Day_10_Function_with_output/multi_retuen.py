def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    else:
        fname = f_name.title()
        lname = l_name.title()
        return f"{fname} {lname}"

fname = input("What is your first name? ")
lname = input("What is your last name? ")

formatted_name = format_name(fname, lname)

if formatted_name == None:
    print("You have not entered either your first name or last name. Try Again.")
else:
    print(f"The result is: {formatted_name}")