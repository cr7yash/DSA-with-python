import Queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
        
newBT = TreeNode("drinks")
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')

newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preorderTraversal(rootNode):
    if not rootNode:
        return
    
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)
    

preorderTraversal(newBT)

def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)
    
def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftChild)
    postorderTraversal(rootNode.rightChild)
    print(rootNode.data)
        
def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
                
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

        
def searchBT(rootNode,nodeValue):
    if not rootNode:
        return
    customQueue = Queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if(root.value.data == nodeValue):
            return "Success"
        if(root.value.leftChild is not None):
            customQueue.enqueue(root.value.leftChild)
                
        if(root.value.rightChild is not None):
            customQueue.enqueue(root.value.rightChild)
        
        return "Not found"
    

def insertNodeBT(rootNode,newNode):
    if not rootNode:
        return
    else:
        customQueue = Queue.Queue()
        customQueue.dequeue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
        
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successful insert"
            
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successful insert"


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
                
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestnode = root.value
        return deepestnode

def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value is None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

                    
def deleteNodeBT(rootNode,node):
    if not rootNode:
        return
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dnode = getDeepestNode(rootNode)
                root.value.data = dnode.data
                deleteDeepestNode(rootNode,dnode)
                return "The node is deleted"
            
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
                
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

                
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Binary tree is deleted"
    
                        

            

    
    