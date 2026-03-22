import re

def check_password(password):
    score = 0

    # length check
    if len(password) >= 8:
        score += 1

    # uppercase
    if re.search("[A-Z]", password):
        score += 1

    # lowercase
    if re.search("[a-z]", password):
        score += 1

    # number
    if re.search("[0-9]", password):
        score += 1

    # special character
    if re.search("[@#$%^&*!]", password):
        score += 1

    # result
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


while True:

    password = input("Enter password: ")

    result = check_password(password)

    print("Password Strength:", result)

    choice = input("Check again? (y/n): ")

    if choice.lower() != "y":
        print("Program ended")
        break