"""THE FUNCTIONS IN THIS FILE ARE ONLY USED TO STOP IT FROM 
THROWING ERRORS , THEY DON'T WORK THEY ARE ONLY FOR THE LEARNING 
PURPOSE"""


"""15"""    #file reading
"""34"""    #strip , split() , isdigit()
"""55"""    #timer
"""66"""    #flag approach
"""74"""    #unpacking of tuple
"""84"""    #escape sequence characters and row string
"""100"""    #match cases
"""108"""    #doc string
"""124"""    #next function 
"""138"""    #enumerate
"""165"""    #better method of flag approach -> use else with loops 
"""178"""    #short hand if else
"""185"""    #global and local variable
"""***"""    #seek(),tell(),truncate()
"""***"""    #lamda function (anonymos function)
"""***"""    #map() , filter() , reduce()
"""***"""    #is vs == 


"""in file reading we have option of reading the whole line or 
we can read line by line and character by character as well"""
def file():
    file = "assume this is a file with some \
    content so after opening it we can do the things shown"
    if "learning" in file:
        print("yes it exists in this file")       #it reads the whole file
    else:
        print("this does not exit")

    for line in file:     #this will read line line by line in a loop
        pass

    for line in file:
        for char in line:  #this will read character by character
            pass
    
    file.seek(6)  #this puts the cursor on the 6 char/byte in the file
    file.tell() #this tells where the cursor is
    file.truncate(7)    #this will truncate the file to 7 char/bytes



"""2. strip() , split() , isdigit()"""
def strip_function():
    var = "      hello world        "
    print(var.strip())   #it will remove unnessary spaces

def split_function():
    var2 = "hello,world,this,is,me"
    print(var2.split(sep="," , maxsplit=5))
    #sep and maxsplit both are optional 
    #default value for sep is space and maxsplit is all
    #returns list with string type elements

def isdigit_function():
    """checks whether the number is digit or not
    if you give a int that is of str type make sure it
    is trimmed then it will return true"""
    var4 = "2642"
    print(var4.isdigit())



"""here we are going to see how we can calculate time of our code
excution"""
def timer():
    import time
    start_time = time.time()
    list2 = (1,2,3,5,6,7,8)
    for val in list2:
        print(val)
    print(f'{time.time()-start_time}')  #it will give the time it took


"""flag approach -> DYI"""
"""unpacking of tuple"""
tup1 = (("jan",1212),("feb",2323),("march",8765))
for month,amount in tup1:
    print(f'{month} and {amount}')
    #this is cool right


"""some common escape sequence characters in python language"""
#a raw string ignores the escape sequence characters
#next line  \n
#tab  \t
#single slash \\
#\'  and  \"
#\r  and \b  one owerwtites the functions and other is used for backspace



"""MATCH - CASES -> they are better at readability ,faster
 great for exact
 matches but have limitation that we can not use the normal 
 mathematical comparison 
 """
def matcher():
    day = ("monday","tuesday","wednesday","thursday","friday","saturday")
    match day:
        case "monday":
            print("bad day")
        case "tuesday":
            print("okay okay")
        case _:         #works like a else statement
            print("no data given")


"""DOC STRING -> used in a function to define it write it in
a first line of the function to execute and that too in 
i ways we write a multi line comment"""
def doc_string():
    print(__doc__()) #argument -> function name
    help()  #argument -> function name


"""ENUMERATE FUNCTION -> it fetches the ind and val from a iterable
and it is a iterator so i does not return any value until or unless
you are using for loop to print for each iteration or you store the 
iterations in a list"""
#enumerate(iterable, start=0)   you can choose the starting point of index
def enumerate_iterator():
    my_list = ["apple", 42, "banana", 99, "cherry"]
    for ind , val in enumerate(my_list):
        print(f'index : {ind} and value : {val}')

    list_of_tuples = list(my_list)
    print(list_of_tuples)




"""NEXT FUNCTION -> this function gives the the value where the 
iterator is iterating at the moment 
next(iterator,default)   default is the value you get when the iterator
#is exhausted to stop the StopIteration exception"""
def error_handling():
    def next_function():
        my_list = ["apple", 42, "banana", 99, "cherry"]
        iterator = iter(my_list)   #iter function makes iterable iterator
        print(next(iterator))
        print(next(iterator))




    """ERROR HANDLING -> used to handle error so the program 
    does not stops or crash"""
    try:
        num = int(input("Enter a number: "))  # Might raise ValueError
        
        if num < 0:
            raise ValueError("Negative numbers are not allowed!")
            # Manually raising an error
        print(10 / num)  # Might raise ZeroDivisionError

    except ValueError as e:
        print(f"ValueError: {e}")
          # Handles invalid input or manually raised ValueError
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print("No errors occurred!")
          # Runs only if no exception happens
    finally:
        print("Done executing.")

    #else is written before finally



"""IF ELSE IS USED WITH LOOPS THEN IT WILL ONLY BE EXECUTED ONLY WHEN THE 
LOOP IS OVER ADN IF LOOP BREAKS IN BETWEEN THE ITERATION THEN THE ELSE 
STATEMENT IS NOT GOING TO BE EXECUTED"""

for i in range(0,8):
    print(i)
    if i == 6:  #because we are breaking the loop it won't execute
        break
else:
    print("the loop is over")



"""short hand if else statements"""
a = 5
b = 3
print("harry") if a<b else print("carry") if b > a else print("khemesh")


"""a local variable and global variable both are different even if they 
are stored with the same name to make sure that you want to use the 
global variable you can specify it using global keyword"""

"""yes guys it is possible you can give function a function as 
an argument"""











