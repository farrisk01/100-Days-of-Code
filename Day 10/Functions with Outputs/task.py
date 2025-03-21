fname = input("Enter first name: ")
lname = input("Enter last name: ")

def format_name(first_name, last_name):
    """"This function takes a first and last name and returns them in Title case."""
    return f"{first_name.title()} {last_name.title()}"

print(format_name(fname, lname))