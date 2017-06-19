class Node(object):

    def __init__(self,data):
        self.data = data
        self.nextNode = None

class Linkedlist(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self, data):

        if self.head is None:
            return

        self.size = self.size - 1

        currentNode = self.head
        prev = None

        while currentNode.data != data:
            prev = currentNode
            currentNode = currentNode.nextNode

        if prev is None:
            self.head = currentNode.nextNode
        else:
            prev.nextNode = currentNode.nextNode

    # O(1)
    def size1(self):
        return self.size

    # O(N)
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size +=1
            actualNode = actualNode.nextNode

        return size
    # O(N)
    def insertEnd(self, data):
        self.size = self.size+1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

linkedlist = Linkedlist()
linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(13)
linkedlist.insertEnd(50)
linkedlist.traverseList()

print("size = %d"%linkedlist.size1())

linkedlist.remove(122)
linkedlist.remove(12)
linkedlist.traverseList()