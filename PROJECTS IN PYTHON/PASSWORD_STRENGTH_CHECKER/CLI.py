import string
lowercase_letter = list(string.ascii_lowercase)
uppercase_letter = list(string.ascii_uppercase)
sum = 0
user_password = input("put in your password -> ")


lowercase_checking = False
uppercase_checking = False
def CaseChecker():
    global sum
    global lowercase_checking
    for val in lowercase_letter:
        if val in user_password:
            sum += 2
            lowercase_checking = True
            break
    
    for val in uppercase_letter:
CaseChecker()
print(sum)