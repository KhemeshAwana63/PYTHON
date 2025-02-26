"""HERE WE ARE GOING TO SEE HOW WE CAN IMPLEMENT LINKED LIST TO PYTHON BECUASE PYTHON DOES NOT 
HAVE AN IN BUILT LINKED LIST"""

class Nodes:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node
"""let us now make some nodes and will then manually tell that these nodes are linking other nodes with
them"""
#'3'->'5'->'8'

node1 = Nodes(3)       #node with data equals 3
node2 = Nodes(5)         #node with data equals 5
node3 = Nodes(8)       #node with data equals 8

node1.next_node = node2    #node1 links to node2
node2.next_node = node3     #node1 links to node2

"""to visualize this we are gonna run a loop and see how one node is pointing towards the next node"""
current_node = node1
while True:
    print(current_node.data,"->",end = " ")
    if current_node.next_node is None:
        print("none")
        break
    current_node = current_node.next_node


