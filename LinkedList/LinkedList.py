# Creating the Node Class
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


# Creating the Nodes
a = Node(5)
b = Node(10)
c = Node(15)
d = Node(20)
e = Node(25)

# Establishing the relationship between nodes.
a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

# Setting the current node. In this example, it is set to the first node, or a.
currentNode = a

# Printing through the Node list starting with the currentNode. It prints the value of the Node.
while currentNode is not None:
    print(currentNode.value)
    currentNode = currentNode.nextNode



