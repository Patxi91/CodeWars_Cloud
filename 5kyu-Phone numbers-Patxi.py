class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        # No Child --> insert
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        # Existing Child --> push it down the tree
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, value):
        self.key = value

    def getRootVal(self):
        return self.key

def pre_count(tree):
    count = 0
    if tree:
        count += 1
        pre_count(tree.getLeftChild())
        pre_count(tree.getRightChild())
    return count

def phone_number(phone_numbers):
    root = BinaryTree('')
    currNode = root
    for num in phone_numbers:
        currNode = root
        for digit in num:
            if (currNode.getLeftChild() or currNode.getRightChild()) and digit != currNode.getLeftChild().getRootVal() and digit != currNode.getRightChild().getRootVal():
                if currNode.getLeftChild().getRootVal() == None:
                    currNode.insertLeft(digit)
                    currNode = currNode.getLeftChild()
                else:
                    currNode.insertRight(digit)
                    currNode = currNode.getRightChild()
            else:
                if digit == currNode.getLeftChild().getRootVal():
                    currNode = currNode.getLeftChild()
                else:
                    currNode = currNode.getRightChild()
    return pre_count(root)


phone_numbers = ['01', '02', '03']
r = phone_number(phone_numbers)