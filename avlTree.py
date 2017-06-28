class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max (self.calcHeight(node.rightChild), self.calcHeight(node.leftChild))

        return self.violation(data, node)

    def violation(self, data, node):

        balance = self.calcBalance(node)
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy..")
            return self.rightRotation(node)
        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy..")
            return self.leftRotation(node)

        if balance > 1 and data > node.leftChild.data:
            print("left right heavy..")
            node.leftChild = self.leftRotation(node.leftChild)
            return self.rightRotation(node)

        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy..")
            node.rightChild = self.rightRotation(node.rightChild)
            return self.rightRotation(node)

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self, node):

        if node.leftChild:
            self.traverseInorder(node.leftChild)

        print("%s" % node.data)

        if node.rightChild:
            self.traverseInorder(node.rightChild)

        print("%s" % node.data)

    def calcHeight(self, node):

        if not node:
            return -1
        return node.height

    # return greater than 1 : rotation이 필요하다 -> left heavy tree -> right rotation
    #       < -1 right heacy -> left lotation
    def calcBalance(self, node):

        if not node:
            return 0

        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rightRotation(self, node):

        print("right rotation ",node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild.height), self.calcHeight(node.rightChild.height)) + 1
        tempLeftChild.height =  max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild

    def leftRotation(self, node):

        print("left rotation ", node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.leftChild.height), self.calcHeight(node.rightChild.height)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild),
                                   self.calcHeight(tempRightChild.rightChild)) + 1

        return tempRightChild

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.traverse()
