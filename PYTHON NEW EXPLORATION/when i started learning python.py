# print('hello world')
# var = None
# print(type(var))
# print(not True)
# print(4>3 and 5>6)
# print(4>3 and 5<6)
# a = 1        #use of type casting to manually change the data type
# b = "2"
# c = int(b)
# print(a + c)
                                    #check how to convert the string in decimal no then you will use 10 as base
# a = int(input("put in your input"), )      #that is how we use the input function
# print(a)




#WAP to input 2 numbers and print sum
# a = int(input())
# b = int(input())
# print(a+b)
#WAP to input side of a square and print its area
# a = int(input())
# print(a**2)
#WAP to input 2 floating point number and print their average
# a = float(input())
# b = float(input())
# print((a+b)/2)
# a = 'khemesh awana gurjar'       #this is how we use indexing and slicing
# print(a[3])
# print(a[0:7])
# str = 'i am coder'
# print(str.endswith('er'))
# print(str.capitalize())
# print(str.replace('am','love'))
# print(str.find('am'))
# print(str.count('am'))

#WAP to check if a no entered by the user is odd or even
# a = int(input('put in the number',))
# if a%2 == 0:
#     print('even')
# elif a%2 != 0:
#     print('odd')
# else:
#     print('bhai yeh to kuch nirala hai')

#grade the students based on their marks
# marks = int(input('put in the marks'))
# if marks >= 90:
#     print('grade','a')
# elif marks <90 and marks >= 80:
#     print('grade','b')
# elif marks <80 and marks>= 70:
#     print('grade','c')
# else:
#     print('grade d')

#WAP to check if a number is a multiple of 7 or not
# a = int(input('put in the no'))
# if a%7 == 0 :
#     print('it is multiple of 7')
# else:
#     print('it is not a multiple of 7')

#WAP to find the greatest of 4 numbers entered by the user
# a = int(input('value',))
# b = int(input('value',))
# c = int(input('value',))
# d = int(input('value',))
# if a > b and a > c and a > d :
#     print('greatest no is', a)
# elif b > a and b > c and b > d:
#     print('greatest no is', b)
# elif c > a and c > d and c > b :
#     print('greatest no is', c)
# elif d > a and d > b and d > c:
#     print('greatest no is', d)


# list = [12, 23,42 , 56.0, 75, 'khemesh', 'gurjar']
# list.insert(1, 'awana')
# list.remove(75)
# list.pop(5)
# list.append('khemesh')
# list.reverse()
# print(list)
#WAP to ask user to input to enter names of thier 3 favorite movies and store them in list
# list = []
# a = input('name of the movie',)
# list.append(a)
# b = input('name of the movie',)
# list.append(b)
# c = input('name of the movie',)
# list.append(c)
# print(list)
#WAP to check if a list contains a palindrome of elements (use copy method)
# list = ['racecar']
# list2 = list.copy()
# list2.reverse()
# if list2 == list:
#     print('it is a palindrome')
# else:
#     print('it is not a palindrome')
#WAP to count the no of students with the 'a' grade in the following tuple
# list = [ 'c','a','a','b']
# print(list.count('a'))
#store the above values in a list and short them from 'a' to 'd'
# list = [ 'c','a','a','b']
# list.sort()
# print(list)










info = {
    'khemesh':'karishma',
    'molu': 78,
    'subject':['physics','mathematics','chemistry'],
    'age': 45,
    657.8: 786,
    'dhoom':{'film1':'amazing',   #this is nested dictionary , we could also put list or tuple in value 
    'film2':89}               #but we can not put list in key because list is mutable 
}
# info['food'] = 'chane'   #it will add a new key value pair
# info['molu'] = 87        #it will change the value of existing value pair
# print(type(info))        #it will  show the type of my dictionary
# print(len(info))           #it will print the length of the dictionary
# info2 = {}               #it is a null dictionary
# print(info['khemesh'])   # if you want to print value of key
# print(info['dhoom']['film1'])  # if there is nested dictionary and you want its key value pair (better then (getkey))
# print(info['subject'][2])      #but if there is a tuple or list then you define the indices not the key
#here is the list of all the methods used with dictionary

# print(info.keys())        #it will return all the keys
# print(info.values())      #it will return all the values
# print(info.get('molu'))   #it will return the value of the key assigned
# new_info = {'awana':'jee'}  #this is to append a dictionary in the existing one
# info.update(new_info)
# print(info)

#now we are staring with sets
collection = {4 , 5, 6, 8, 'khemesh','karishma',678.866,5,5}
# print(type(collection))
# print(len(collection))
collection1 = set() #this creates a empty set
#here is the list of all the messages related to sets
# collection.clear()     #this makes the whole set empty and you can't put arguments in bracket
# collection.pop()       #removes a random value
# collection.union(collection1)    #this is to take union of two sets
# collection.intersection(collection1)  #intersection

# #store the following word meanings in a python dictionary 
# # table: 'a piece of funiture' , 'list of facts and figures'
# # cat : 'a small animal'
# dict = {
#     "table":("a piece of funiture", "list of facts and figures"),
#     "cat": "a small animal"
# }
# print(dict)

# you are given a list of subjects for students . assume one classroom is required for 1 subject . 
# how many classrooms are needed by all students
# "python ","java","C++","javascript","java","java","python", "C++", "C","python"
# set = { "python ","java","C++","javascript","java","java","python", "C++", "C","python"}
# print(len(set))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary start with an empty dictionary and add one by one 
# subject name as key and  marks as value
# dict = {}
# dict["physics"] = int(input("put how much marks you want to assign",))
# dict["chemistry"] = int(input("put how much marks you want to assign",))
# dict["mathematics"] = int(input("put how much marks you want to assign",))
# print(dict)

#figure out a way to store 9 and 9.0 as separate values in the set (you can take help of built in data types)
# set = {9 , "9.0"}
# print(set)














#in looping it will keep performing the task in the loop untill the condition that you gave is returning false
# khemesh = 1
# while khemesh <= 6:
#     print('gurjar')
#     khemesh += 1
#now we are gonna see how the value of variable was changing after each iteration of the loop
# khemesh = 1
# while khemesh <= 6:
#     print('gurjar' , khemesh)  #here in print we have inserted khemesh as well to see how the value of
#     khemesh += 1                khemesh variable was changing with each iteration

#print the element of the following list using a loop [1 , 4, 9, 16, 25, 36, 49, 64]
# a = 1
# while a <= 8:
#     print(a**2)
#     a += 1
#another method is , as we know we can either print the elements of this list using their index position
#but in that case we wiill have to write many print statements , here is another way
# khemesh = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] #this method can print any kind of values in the list
# ind = 0
# while ind < len(khemesh):
#     print(khemesh[ind])
#     ind += 1  #here we are variying the value of ind in the list in the print statement

#print numbers from 1 to 100
# a = 1 
# while a < 101:
#     print(a)
#     a += 1

#print numbers from 100 to 1
# a = 100
# while a >= 1:
#     print(a)
#     a -= 1

#print the multiplication table of a number n
# n = int(input('the number'))
# a = 1
# while a <= 10:
#     print(n*a)
#     a += 1

#search for a number n in this group (tuple) using loop 
# a = (1, 4, 9, 16, 25, 36, 49, 64)
# n = int(input('give the number to search'))
# ind = 0
# while ind < len(a):
#     if (a[ind] == n):                          why an equal to sign won't give us the answer
#        print('found the index',ind)
#     ind += 1

#print hello 5 times
# n = 1
# while n <= 5:
#     print('hello')
#     n += 1

#print numbers from 1 to 5
# n = 1
# while n <=5:
#     print(n)
#     n += 1

#show infinite , iterator
# n = 1
# while n < 2:
#     print('khemesh')

#take search example and stop the search when found
# n = 6
# a = 2
# while a < 10:
#     if a == n:
#         print('found')
#         break
#     else:
#         print('finding')
#     a += 1

#print all numbers but not multiple of 3
# a = 0
# while a < 31:
#     if a%3 == 0:
#         a += 1                      this line is very important because if condition without a task
#         continue                    is not going to be considered
#     print(a)
#     a += 1

#print elements of the following list using a loop 
# tup1 = [1 , 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in tup1:
#     print(val)

#search for a number n in this tuple
# tup1 = [1 , 4, 9, 16, 25, 36, 49, 64, 81, 100]
# n = int(input('the number that you want to see index of'))
# ind = 0
# for val in tup1:
#     if n == val:
#         print('found the index is',ind)
#     ind += 1

#print the multiplication table of a number n
# n = int(input('put the number'))
# for val in range(1,11):
#     print(n*val)

#wap to find the sum of 1st n natural no. (using while)
# a = int(input('the number'))
# i = 1
# sum = 0
# while i < a:
#     sum += i
#     i += 1
# print(sum)

#wap to find teh factorial of first n natural numbers (using for)
# sum = 1
# a = int(input('the numbers'))
# for val in range(1,a+1):
#     sum *= val
# print(sum)













#waf to find the factorial of n (n is a parameter)
# def factorial_maker(a):
#     i = a - 1
#     while i > 0:
#         a*= i                 #use a different way of doing it in shorter lines of code
#         i -= 1
#     print(a)
#     return a

# factorial_maker(5)

#waf to print the length of a list (list is the parameter)
# def length(list):
#     i = 0
#     for val in list:
#         i += 1
#     print(i)
#     return i

# tup = [1,2,3,4,5,6,7,8,9]
# length(tup)

#waf to print the elements of a list in a single line (list is the parameter)
# def single_line(list):
#     for item in list:                    #if you see an % sign then put a extra print statement in the end 
#         print(item, end = " ")           #also look for the reason why it happend

# yo =["python ","java","C++","javascript","java","java","python", "C++", "C","python"]
# single_line(yo)
    
#waf to convert USD to INR
# def convertor(a):
#     b = a*88.88
#     c = print(b,"INR")
#     return c

# convertor(67)

#waf to find whether a number is even or odd
# def checker(a):
#     b = "even number"
#     c = "odd number"
#     if a%2 == 0:
#         print(b)
#         return b
#     else:
#         print(c)
#         return c

# checker(87)
#example of resursive fuction
# def fun(n):
#     if n == 0:
#         return
#     print(n)
#     sum(n-1)
#     print('end')

# fun(8)

#waf to calculate a factorial of n

#waf to calculate the sum of first n natural numbers
# def sum(n):
#     if n == 0:
#         return 0
#     return sum(n-1) + n

# print(sum(10))

#write a recursive function to print all the elements in a list 
# def printlist(list , ind=0):
#     if ind == len(list):
#        return 
#     print(list[ind],end = ' ')
#     printlist(list , ind + 1)


# tup = ['khemesh', 'karishma', 'molu']
# printlist(tup)


















# f = open("demo.txt","r",)        example of how these things are done
# data = f.read()
# print(data)
# f.close()


# import os 
# print(os.path.exists("demo.txt"))   #this will tell if the file exists
# file = open("demo.txt","r")          #this will give some information about the file
# print(file)
# with open("demo.txt","r") as file:         #this is to put the cursor in the beginning again
#     file.seek(0)
#     a = file.read()
#     print(a)
# with open("demo.txt","r") as file:             #this shows if there are any hidden characters in the files
#     content = file.read()
#     print(repr(content))
# import os                                       #this is to check the size of file if it shows zero you file is
# print(os.path.getsize("demo.txt"))              #effectively empty
# with open("demo.txt","w") as file:                                           #this will overwrite
#     file.write("bhai kuchh samajh nahi aa raha ki kya problem ho rhi h")

# with open("practice.txt","w") as file:
#     file.write(str.replace("java" , "python"))       #that is not how you do this
#search if the word "learning" exists in the file or not
# with open("practice.txt","r") as files:
#   data = files.read()
# if data.find("learning") != -1:
#    print("yes it exists")

#convert your last and last second question into a function that checks the word
#waf to find in which line of the file does the word "learning" occurs first 
# class Student:
#     name = "karan"         #this is an example of an simple class and object
#                                 #where we have used an in built constructor
# s1 = Student()
# print(s1.name)
# class student:
#     collage_name = "apna college"
#     def __init__(self,fullname):
#         self.name = fullname                   #here we have used class object with a user defined 
#                                                          #constructor and we are also seeing the concept of
# s1 = student("karan")                                          #class.attribute and object.attribute
# print(s1.name)
# s2 = student("bruce")
# print(s2.name)
# print(s1.collage_name , s2.collage_name)
# print(student.collage_name)               #here we are seeing the class.attribute's value directly 
                                                 #instead of indirectly seeing it with object

# class student:
#     collage_name = "apna college"
#     def __init__(self,fullname):
#         self.name = fullname
#     def welcome(self):                            #we can give our objects methods as well which will tell 
#         print("or bhai badhiya")                       #what these objects can do

# s1 = student("karan")
# s1.welcome()

#create student class that takes name and marks of 3 subjects as arguments in constructor then
#create a method to print the average
# class students:
#     def __init__(self,sub1,marks,sub2,marks2,sub3,marks3):
#         self.subject = sub1
#         self.marks = marks
#         self.subject = sub2                         #this was my way of doing things 
#         self.marks = marks2
#         self.subject = sub3
#         self.marks = marks3
#     def average(self,sub1,marks,sub2,marks2,sub3,marks3):
#         print((marks + marks2 + marks3)/3)
# s1 = students('physics',78,'chemistry',86,'maths',67)
# s1.average("physics",78,"chemistry",86,"maths",67)

# class students:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def average(self):                           this was shraddhas method
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(sum/3)
# s1 = students("karan",[67,87,78])
# s1.average()

# create account class with 2 attributes - balance and account no.
# class account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no
# karan = account(675,64758336)
# print(karan.balance)

# create methods for debit , credit , and printing the balance
class bank_balnace:
    def __init__(self,balance):
        self.balance = balance
    def debit(self,expense):
        self.balance -= expense
        print("rs",expense,"was debited")
    def credit(self,value):
        self.balance += value
        print("rs",value,"was credit")
    def getbalance(self):
        return self.balance

mukesh = bank_balnace(786)
mukesh.debit(76)             #this one is giving debited balance
print(mukesh.balance)            #this one is giving the starting balance


# #now we are going to see what is the right method to do it
#firstly we were supposed to do it with the 1st question 
# class account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def debit(self,amount):
#         self.balance -= amount
#         print("rs",amount,"was debited")
#         print(self.getbalance(),'rs is the total balance')           #this was shraddhas method

#     def credit(self,amount):
#         self.balance += amount
#         print('rs',amount,"was credited")
#         print(self.getbalance(),'rs is the total balance')

#     def getbalance(self):
#         return self.balance

# karan = account(789,87653)
# karan.debit(87)
# karan.getbalance()
# print(karan.balance)



# class bank_balnace:
#     def __init__(self,balance):
#         self.balance = balance
#     def debit(self,expense):
#         print(self.balance - expense)
#     def credit(self,value):
#         print(self.balance - value)
#     def getbalance(self):
#         return self.balance

# mukesh = bank_balnace(786)
# mukesh.debit(76)
# print(mukesh.balance)  
print("khemesh is the guy")
    









    



    



















