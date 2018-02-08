class node:
    def __init__(self, data, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild
    def inOrder(self):
        if(self.leftChild!=None):
            self.leftChild.inOrder()
        print(self.data)
        if(self.rightChild!=None):
            self.rightChild.inOrder()
    def preOrder(self):
        print(self.data)
        if(self.leftChild!=None):
            self.leftChild.preOrder()
        if(self.rightChild!=None):
            self.rightChild.preOrder()
    def postOrder(self):
        if(self.leftChild!=None):
            self.leftChild.postOrder()
        if(self.rightChild!=None):
            self.rightChild.postOrder()
        print(self.data)

def lrtraversal(n):
    output={}
    def traversal(n, pos):
        nonlocal output
        if pos in output:
            output[pos].append(n.data)
        else:
            output[pos] = [n.data]
        if n.leftChild!=None:
            traversal(n.leftChild, pos-1)
        if n.rightChild!=None:
            traversal(n.rightChild, pos+1)
    traversal(n,0)
    for key in sorted(output.keys()):
        print(output[key])
    


        

x = node(5)
x.leftChild = node(3)
x.rightChild = node(7)
x.rightChild.leftChild = node(9)

lrtraversal(x)
