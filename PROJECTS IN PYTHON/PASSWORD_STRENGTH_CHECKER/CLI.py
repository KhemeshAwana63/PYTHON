import string

PasswordCriteria = {"Uppercase letter":list(string.ascii_uppercase), 
                    "Lowercase letter": list(string.ascii_lowercase), 
                    "Number": list(string.digits), 
                    "Special character": list(string.punctuation),}

PasswordType = {5: "Weak password",
                10: "Medium password",
                15: "Strong password"}
points = 0

def TotalPoint(InputPassword):
    global points
    length_of_password = len(InputPassword)
    for char in InputPassword:
        if char in PasswordCriteria["Uppercase letter"] or char in PasswordCriteria["Lowercase letter"]:
            points += 1
        elif char in PasswordCriteria["Number"]:
            points += 3
        elif char in PasswordCriteria["Special character"]:
            points += 5
        else:
            points += 1
    if length_of_password <= 5:
        points += 1
    elif length_of_password > 5 and length_of_password <= 10:
        points += 3
    elif length_of_password > 10:
        points += 5


def password_strenth(points):
    if points <= 5:
        print(PasswordType[5])
    elif points <= 10 and points > 5:
        print(PasswordType[10])
    elif points > 10:
        print(PasswordType[15])

def main():
    while True:
        InputPassword = input("Enter your password: ").strip()
        if InputPassword == "":
            print("Please give some input to evaluate")
            continue
        else:
            break

    TotalPoint(InputPassword)
    password_strenth(points)

main()
