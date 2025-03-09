"""HERE IS THE COMMAND LINE INTERFACE FOR THE TO DO LIST"""
import json
#making a empyt dictionary to store data
tasks = {"Studies":[],
         "Diet":[]}
options = ["ADD","DELETE","VIEW"]

def AddTask(added_task):
    while True:
        key = input("where do you want to add the task -> ").capitalize()
        if key not in tasks.keys():
            print("choose the valid option")
            continue
        else:
            tasks[key].append(added_task)
            # SaveTask()
            print(f'task added in {key} section')
            break

# def SaveTask():
    # with open

    # pass
def main():
    while True:
        print("what do you want to do :\n"  
        "ADD\n"
        "DELETE\n"
        "VIEW")
        inp = input("put in the task-> ").upper()
        if inp not in options:
            print("invalid options ...plz chose the correct option")
            continue

        elif inp == "ADD":  #add function and break call
            added_task = input("-> ")
            AddTask(added_task)
            break

        elif inp == "DELETE": #add function and break call
            pass

        elif inp == "VIEW": #add function and break call
            pass

main()
print()













