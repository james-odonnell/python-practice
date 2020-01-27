class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode



a = Node(5)
b = Node(10)
c = Node(15)
d = Node(20)
e = Node(25)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e


currentNode = a

while currentNode is not None:
    print(currentNode.value)
    currentNode = currentNode.nextNode



