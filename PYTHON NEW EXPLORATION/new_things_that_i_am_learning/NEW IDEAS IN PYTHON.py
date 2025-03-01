#file reading
#strip , split(integer , list) , isdigit(trim , integer)
#timer
#flag approach
#unpacking of tuple

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







