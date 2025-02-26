"""HERE WE HAVE THE EXPALANATION OF THE METHOD 2"""
# class Nodes:                #creating this class because when we will be adding
#     def __init__(self, data, next=None):   #new node in linked list we will need this
#         self.data = data
#         self.next = next

# class linkedlist:       #makeing this to fill in many nodes in here , initially keeping
#     def __init__(self,head = None):   #it empty and by add method we will fill it
#         self.head = head
    
#     def insert(self,data):     #this is gonna make a new node and if linkedlist is empty it will
#         node = Nodes(data)        #make that node its head but if the linkedlist is not empty
#         if self.head is None:
#             self.head = node
#             return
#         else:                          #then this will run 
#             current_node = self.head    
#             while current_node.next:     #it checks if .next exists if exists it will go to the
#                 current_node = current_node.next   #next node and so on but if not .next does
#             current_node.next = node        #not exist then it will make the new node the next 
#                                             #node of the node that is latest in the loop
#     def printlinkedlist(self):
#         current_node = self.head                    #this is made just to display the link
#         while current_node:
#             print(current_node.data,end = "->")
#             current_node = current_node.next
#         print('none')
         #here we are storing the self.head in a variable because self.head is not returning any
         #printable value as you can see in the other methods/function



"""HERE WE ARE GOING TO SEE THE SECOND METHOD THAT IS USED IN PYTHON
TO IMPLEMENT LINKED LIST IN PYTHON"""
class Nodes:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self,head = None):
        self.head = head
    
    def insert(self,data):
        node = Nodes(data)
        if self.head is None:
            self.head = node
            return
        else:
            current_node = self.head    
            while current_node.next:
                current_node = current_node.next
            current_node.next = node 
    def printlinkedlist(self):
        current_node = self.head 
        while current_node:
            print(current_node.data,end = "->")
            current_node = current_node.next
        print('none')

ll = linkedlist()
ll.insert(5)
ll.printlinkedlist()
ll.insert(89)
ll.printlinkedlist()



