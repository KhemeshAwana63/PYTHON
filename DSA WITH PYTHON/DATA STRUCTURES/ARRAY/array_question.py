#HERE IS THE 5 QUESTONS BASED ON ARRAYS
list1 = [2200,2350,2600,2130,2190]
list2 = [('jan',2300),('feb',2350),('mar',2600),('apr',2130),('may',2190)]
list3 = [['jan',2300],['feb',2350],['mar',2600],['apr',2130],['may',2190]]
"""1. In Feb, how many dollars you spent extra compare to January?"""
print("you spent",list1[1]-list1[0],"extras in feb in comparison to jan")

"""2.Find out your total expense in first quarter (first three months) of the year"""
total_expense = 0
for val in list1:
    if val == 2130:
        break
    total_expense += val

print(total_expense)
# time complexity for this function is O(1)

"""3.Find out if you spent exactly 2000 dollars in any month"""
found = False
for val in list2:
    if 2000 in val:
        print(val[0],"has exactly 2000 rupee expenses")
        found = True
if not found:
    print("no month has excatly 2000 rupee expenses")

"""4.June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list"""
list2.append(('jun',1980))
print(list2)

"""5.You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""
list3[3][1] = list3[3][1] + 200
print(list3)
 



 # HERE IS ANOTHER 6 QUESTIONS BASED ON ARRAYS
heros=['spider man','thor','hulk','iron man','captain america']

"""1. Length of the list"""
print(len(heros))       #time complexity is O(n)

"""2. Add 'black panther' at the end of this list"""
heros.append('black panther')
print(heros)            #time complexity is O(n)

"""3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'"""
heros.remove('black panther')      
heros.insert(3,"black panther")     #time complexity is O(n)
print(heros)

"""4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code."""
heros[1:3] = ["doctor strange"]         #we have to give list to a list
print(heros)

"""5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""
heros.sort()
print(heros)

"""6.Create a list of all odd numbers between 1 and a max number. Max number is something 
you need to take from a user using input() function
"""
n = int(input("put the max number here"))
list4 = list(range(1,n+1,2))
print(list4)