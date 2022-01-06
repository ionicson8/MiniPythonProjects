class Node:
    def __init__(self, datum: int=None, nextNode=None):
        self.datum = datum
        self.nextNode = None

class LinkedList:
    def __init__(self, headNode):
        self.headNode = headNode

    def printList(self):
        next = self.headNode

        while next is not None:
            print(next.datum)
            next = next.nextNode

test1 = Node(3.2)
test2 = Node(6)
test3 = Node(8)

test1.nextNode = test2
test2.nextNode = test3

testList = LinkedList(test1)

testList.printList()