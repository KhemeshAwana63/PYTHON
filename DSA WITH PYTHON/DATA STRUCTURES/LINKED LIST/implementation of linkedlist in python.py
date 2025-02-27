"""first method of implementation of linkedlist in python (manual)"""
class Nodes:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Nodes(56)
node2 = Nodes(45)
node3 = Nodes(76)
node4 = Nodes(87)

node1.next = node2
node2.next = node3
node3.next = node4

current = node1
while True:
    if current.next is None:
        print("none")
        break
    print(current.data,end ="->")
    current = current.next

"""2ND METHOD OF IMPLEMENTING LINKED LIST IN PYTHON (AUTOMATIC)"""
class Nodes:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self,val=None):
        self.val = val

    def add(self,data):
        node = Nodes(data)
        if self.val is None:
            self.val = node
            return
        else:
            current = self.val
            while current.next:
                current = current.next
            current.next = node

    def printlinkedlist(self):
        current = self.val
        while current:
            print(current.data,end="->")
            current = current.next
        print("none")

ll = linkedlist()
ll.add(87)
ll.add(64)
ll.printlinkedlist()