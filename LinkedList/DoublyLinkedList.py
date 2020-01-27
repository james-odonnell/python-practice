class Node:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

    def get_next(self):
        return self.nextNode

    def get_previous(self):
        return self.prevNode



a = Node("a1")
b = Node("b2")
c = Node("c3")
d = Node("d4")
e = Node("e5")
f = Node("f6", None, e)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e


e.prevNode = d
d.prevNode = c
c.prevNode = b
b.prevNode = a

head = a
currentNode = head

while currentNode is not None:
    if currentNode.prevNode is None:
        print("Current Node Value: " + currentNode.value, " Previous Node Value: " + "None", " Next Node Value: " + currentNode.nextNode.value)
        currentNode = currentNode.nextNode
    elif currentNode.nextNode is None:
        print("Current Node Value: " + currentNode.value, " Previous Node Value: " + currentNode.prevNode.value, " Next Node Value: " + "None")
        currentNode = currentNode.nextNode
    else:
        print("Current Node Value: " + currentNode.value, " Previous Node Value: " + currentNode.prevNode.value, " Next Node Value: " + currentNode.nextNode.value)
        currentNode = currentNode.nextNode



