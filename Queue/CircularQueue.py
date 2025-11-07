class CircularQueue:
    def __init__(self,maxSize):
        self.items = maxSize *[None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    # def enqueue(self,value):
    #     if self.isFull():
    #         return "The Queue is full"
    #     else:
            
        