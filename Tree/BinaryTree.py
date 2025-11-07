class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.maxSize = size
        self.lastUsedIndex = 0

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary tree is full"
        
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        
        return "The value has been inserted"