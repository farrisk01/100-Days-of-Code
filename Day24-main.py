# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def retrieve_names():
    name_list = []
    try:
        with open("/Users/kfarris/PycharmProjects/100-days/Input/Names/invited_names.txt") as f:
                name_list = f.read().splitlines()
        return name_list
    except FileNotFoundError:
        print("File not found")

def retrieve_invite():
    try:
        with open("/Users/kfarris/PycharmProjects/100-days/Input/Letters/starting_letter.txt", 'r') as f:
            file_as_string = f.read()
        return file_as_string
    except FileNotFoundError:
        print("File not found")
def create_invitations():
    name_list = retrieve_names()
    invite = retrieve_invite()
    try:
        for name in name_list:
            with open("/Users/kfarris/PycharmProjects/100-days/Output/ReadyToSend/" + name + ".txt", 'w') as f:
                f.write(invite.replace('[name]', name))
    except:
        print("Failed to create invitations")

create_invitations()

