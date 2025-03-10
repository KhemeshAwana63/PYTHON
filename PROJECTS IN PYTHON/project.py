"""here you will see projects that i have made along the journey in python
as you go down the page you will find my level of coding improved ....i mean that is 
what i am expecting from myself right now when i am 
writing this little message for you guys
so that is it from me ....enjoy my journey of python"""
#THIS IS THE LIST OF FUNCTION(BASICALLY PROJECT STORED IN FUNCTION)
#ROLL_THE_DICE()
#GUESS_THE_NUMBER()
#ROCK_PAPER_SCISSOR()
#CURRENCY_CONVERTER

"""ROLE THE DICE"""
import random
yes = "y"
no = "n"
dice_no = (1,2,3)
choices = (yes , no)
def ROLL_THE_DICE(counter = 0):
    while True:
        input1 = input('do you want to play roll the dice y/n ').lower()
        if input1 not in choices:
            print("choose the valid option")
            continue
        if input1 == yes:
            input2 = int(input("how many dices you want to roll options(1,2,3) "))
            if input2 not in dice_no:
                print("choose the valid option")
                continue
            elif input2 == 1:
                print(random.randrange(1,7))
            elif input2 == 2:
                d1 = random.randrange(1,7)
                d2 = random.randrange(1,7)
                print(f'{d1},{d2}')
            else:
                d3 = (random.randrange(1,7))
                d4 = (random.randrange(1,7))
                d5 = (random.randrange(1,7))
                print(f'{d3},{d4},{d5}')
        else:
            print("thanks for playing, you rolled the dice ",counter,"times")
            break
        counter += 1





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
                if your_chosen == computer_chosen:
                    print(f'match tied computer chose {computer_chosen} and you chose {your_chosen}')
                elif ((your_chosen == "rock" and computer_chosen == "scissor") or
                     (your_chosen == "paper" and computer_chosen == "rock") or
                     (your_chosen == "scissor" and computer_chosen == "paper")):
                     print(f'you won computer chose {computer_chosen} and you chose {your_chosen}')
                else:
                    print(f'you lost computer chose {computer_chosen} and you chose {your_chosen}')
                    continue
        elif taking_input == "n":
            print('thanks for playing')
            break
        else:
            print('choose the valid option')
            continue
"""i am not happy with this to be honest because i think i could have made better
logic for this problem but anyways let it be i will be learning more along the path"""






"""HERE WE ARE BUILDING A CURRENCY CONVERTER CODE THAT WILL TAKE THREE CURRENCY AS
OUTPUT AND WILL RETURN THREE CURRENCY OUTPUT ACCORDINGLY"""

def CURRENCY_CONVERTER():
    while True:
        amount = int(input("put in the amount you want to convert "))
        while True:
            source_currency = str(input("choose the currency type between USD/RUP/EUR")).lower()
            target_currency = str(input("choose the currency type between USD/RUP/EUR in which you want to change in " )).lower()
            if target_currency == source_currency:
                print(f'{amount}{source_currency}is {amount}{target_currency}')
                break
            elif source_currency == "usd" and target_currency == "rup":
                print (f'{amount} {source_currency} is {amount*88} {target_currency}')
                break
            elif source_currency == "usd" and target_currency == "eur":
                print (f'{amount} {source_currency} is {amount*0.9629} {target_currency}')
                break
            elif source_currency == "rup" and target_currency == "usd":
                print (f'{amount} {source_currency} is {amount/88} {target_currency}')
                break
            elif source_currency == "rup" and target_currency == "eur":
                print (f'{amount} {source_currency} is {amount/90} {target_currency}')
                break
            elif source_currency == "eur" and target_currency == "rup":
                print (f'{amount} {source_currency} is {amount*90} {target_currency}')
                break
            elif source_currency == "eur" and target_currency == "usd":
                print (f'{amount} {source_currency} is {amount*1.2} {target_currency}')
                break
            else:
                print("choose the right currency")
        asking_again = str(input("do you want to use the converter again  y/n" )).lower()
        while True:
            if asking_again == "y":
                print("okay")
                break
            elif asking_again == "n":
                break
            else:
                print('choose the valid option')
                continue
        if asking_again == "n":
            print("thanks for playing")
            break






def QUIZ_GAME():
    score = 0  
    questions = [
        {
            'question': 'Doston ke beech hamesha sahi kaun hota hai?',
            'options': ['Khemesh', 'Karan (lekin sirf sapno mein)', 'Koi nahi hota', 'Option 2 ek joke hai'],
            'correct': 'Khemesh'
        },
        {
            'question': 'Kaun sabse zyada plans cancel karta hai?',
            'options': ['Khemesh', 'Karan', 'Dono ek doosre pe ilzaam lagayenge', 'Plan? Kaunsa plan?'],
            'correct': 'Karan'
        },
        {
            'question': 'Zombie attack mein kaun survive karega?',
            'options': ['Khemesh', 'Karan', 'Khemesh kyunki usko dimaag use karna aata hai', 'Dono chhup jaayenge aur bhookha zombie ro dega'],
            'correct': 'Khemesh'
        },
        {
            'question': 'Kaun traffic mein sabse zyada chill rehta hai?',
            'options': ['Khemesh', 'Karan', 'Gaadi', 'Traffic bhi bhaag jayega Bhais ka patience dekh ke'],
            'correct': 'Khemesh'
        },
        {
            'question': 'Kaun jaldi tayyar ho jata hai?',
            'options': ['Khemesh', 'Karan', 'Khemesh, even slow motion mein bhi', 'Karan tayyar hota nahi, tayyar hone ka natak karta hai'],
            'correct': 'Khemesh'
        },
        {
            'question': 'Dosti ka asli boss kaun hai?',
            'options': ['Khemesh', 'Karan', 'Khemesh (Karan sirf maan nahi raha)', 'Karan ko lagta hai wo boss hai'],
            'correct': 'Khemesh'
        },
        {
            'question': 'Kaun hamesha "5 minute" bolke 1 ghanta lagata hai?',
            'options': ['Khemesh', 'Karan', 'Karan, kyunki uska "5 min" ka alag calendar hai', 'Samay khud confuse ho jata hai'],
            'correct': 'Karan'
        },
        {
            'question': 'Movie choose karne mein kaun best hai?',
            'options': ['Khemesh', 'Karan', 'Khemesh, par Karan phir bhi badal dega', 'Remote control bhi thak gaya hai Karan ke choices se'],
            'correct': 'Khemesh'
        },
        {
            'question': 'Cooking competition kaun jeetega?',
            'options': ['Khemesh', 'Karan', 'Delivery wala', 'Smoke detector (Karan ka khaana dekh ke)'],
            'correct': 'Khemesh'
        },
        {
            'question': 'Kaun sabse zyada funny hai?',
            'options': ['Khemesh', 'Karan', 'Khemesh ke jokes legendary hain', 'Karan ka sense of humor bhi ghaas charne gaya hai'],
            'correct': 'Khemesh'
        }
    ]

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer here: ").strip().capitalize()  

        if answer == q["correct"]:
            print("Sahi jawaab! 🔥")
            score += 4
        else:
            print(f"Galat! Sahi jawaab tha: {q['correct']} 😜")
            score -= 2

    print(f"\nAapka final score: {score} out of {len(questions) * 4}")






