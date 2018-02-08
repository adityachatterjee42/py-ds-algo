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
    def isLeaf(self):
        if self.rightChild==None and self.leftChild==None:
            return True
        return False

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

def deepestLeftLeaf(n, depth, isLeft):
    if n.isLeaf() and isLeft:
        return {'data': n.data, 'depth': depth}
    if n.isLeaf() and not isLeft:
        return None
    if n.leftChild!=None:
        leftResult = deepestLeftLeaf(n.leftChild, depth+1, True)
    else:
        leftResult = None
    if n.rightChild!=None:
        rightResult = deepestLeftLeaf(n.rightChild, depth+1, False)
    else:
        rightResult = None
    if leftResult==None and rightResult==None:
        return None
    if leftResult==None:
        return rightResult
    if rightResult==None:
        return leftResult
    if leftResult['depth']>=rightResult['depth']:
        return leftResult
    return rightResult
    



    


        

x = node(5)
x.leftChild = node(3)
x.rightChild = node(7)
x.rightChild.leftChild = node(9)

print(deepestLeftLeaf(x, 0, False))