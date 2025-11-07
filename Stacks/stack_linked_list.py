class Node:
    def __init__(self):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
        
    def push(self,value):
        new_node = Node()
        new_node.next = self.top
        self.top = new_node
        self.length += 1 
        
    def pop(self,value):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def peek(self):
        return self.top
        
    def is_empty(self):
        return self.length == 0
    
    def clear(self):
        self.top = None
        self.length = 0
        
        
new_stack = Stack()