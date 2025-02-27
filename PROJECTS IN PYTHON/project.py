"""here you will see projects that i have made along the journey in python
as you go down the page you will find my level of coding improved ....i mean that is 
what i am expecting from myself right now when i am 
writing this little message for you guys
so that is it from me ....enjoy my journey of python"""
#THIS IS THE LIST OF FUNCTION(BASICALLY PROJECT STORED IN FUNCTION)
#ROLL_THE_DICE()
#GUESS_THE_NUMBER()
#ROCK_PAPER_SCISSOR()

"""ROLE THE DICE"""
import random
def ROLL_THE_DICE():
    a = str(input("do you want to play the roll the dice game y/n")).lower()
    while True:
        if a == "y":
            print(random.randint(1,7))
            b = str(input("do you want to play again y/n")).lower()
            if b == "y":
                continue
            elif b == "n":
                print('thanks for playing')
                break
            else:
                print("put in the valid option, only (y/n) are accepted")
                continue
        elif a == "n":
            print('thanks for playing')
            break
        else:
            print("put in the valid option, only (y/n) are accepted")
            continue
#the nested if condition is just for fun ...i could do it without it as well

"""GUESSING THE NUMBER"""

def GUESS_THE_NUMBER():
    target_no = random.randint(1,101)
    while True:
        guessed_no = int(input("guess a number between 1 to 100" ))
        if guessed_no > target_no:
            print("the number is bigger then the target number")
            continue
        elif guessed_no<target_no:
            print("the number is smaller then the target number")
            continue
        else:
            print("you have guessed the number")
            break

#this is how you make logic for a guess the number type of game

"""ROCK ,PAPER ,SCISSOR"""
def ROCK_PAPER_SCISSOR():
    list = ["rock","paper","scissor"]
    while True:
        taking_input = str(input("do you want to play the game (y/n)")).lower()
        if taking_input == "y":
                your_chosen= str(input("choose between rock/paper/scissor")).lower()
                computer_chosen = random.choice(list)
                if your_chosen == "rock" and computer_chosen == "rock":
                    print("match tied you chose r and computer chose r")
                    continue
                elif your_chosen == "rock" and computer_chosen == "scissor":
                    print("you won you chose r and computer chose s")
                    continue
                elif your_chosen == "rock" and computer_chosen == "paper":
                    print("you loose you chose r and cmputer chose p")
                    continue
                elif your_chosen == "paper" and computer_chosen == "rock":
                    print("you won you chose p and computer chose r")
                    continue
                elif your_chosen == "paper" and computer_chosen == "scissor":
                    print("you loose you chose p and cmputer chose s")
                    continue
                elif your_chosen == "paper" and computer_chosen == "paper":
                    print("match tied you chose p and computer chose p")
                    continue
                elif your_chosen == "scissor" and computer_chosen == "paper":
                    print("you won you chose s and computer chose p")
                    continue
                elif your_chosen == "scissor"and computer_chosen == "scissor":
                    print("match tied you chose s and computer chose s")
                    continue
                elif your_chosen == "scissor" and computer_chosen == "rock":
                    print("you loose you chose s and cmputer chose r")
                    continue
                else:
                    print("put in the valid option")
                    continue
        elif taking_input == "n":
            print('thanks for playing')
            break
        else:
            print('choose the valid option')
            continue
"""i am not happy with this to be honest because i think i could have made better
logic for this problem but anyways let it be i will be learning more along the path"""


        
    
