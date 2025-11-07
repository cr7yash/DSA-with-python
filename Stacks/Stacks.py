class Stack:
    # constructor
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)
        
    def push(self,element):
        # Add to the end of the list
        self.items.append(element)
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        # Clear the stack
        self.items =[]
        
my_stack = Stack()

my_stack.push(5)
my_stack.push(20)
my_stack.push(51)
my_stack.pop()
my_stack.peek()
my_stack.clear()

print(my_stack)