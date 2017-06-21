class Node(object):

    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BSTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            print("node not none")
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    # O(logN) : average  if balance tree
    # O(N) : worst  -> AVL RBT가 필요하다
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def remove(self, data):
        if self.root:
            self.root = self._removeNode(data, self.root)

    def _removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self._removeNode(data, node.leftChilde)
        elif data > node.data:
            node.rightChild = self._removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:  # leaf node
                print("remove leaf node")
                del node
                return None
            if not node.leftChild:
                print("removing a node with a single right child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                return tempNode
            print("removing node with 2 children")
            tempNode = self.getProcedecor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self._removeNode(tempNode.data, node.leftChild)

        return node

    def getProcedecor(self, node):
        if node.rightChild:
            return self.getProcedecor(node.rightChild)
        return node

    def getMinValue(self):
        if self.root:
            return self._getMin(self.root)


    def _getMin(self, node):


        if node.leftChild:
            return self._getMin(node.leftChild)

        return node.data


    def getMaxValue(self):
        if self.root:
            return self._getMax(self.root)


    def _getMax(self, node):
        if node.rightChild:
            return self._getMax(node.rightChild)
        return node.data


    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("%s " % node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)


bst = BSTree()
bst.insert(10)
bst.insert(8)
bst.insert(15)
bst.insert(9)
bst.insert(1)
bst.insert(20)
bst.insert(11)

print("min :",bst.getMinValue())
print("max :",bst.getMaxValue())
bst.traverse()

bst.remove(15)
bst.traverse()