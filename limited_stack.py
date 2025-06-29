class Stack:
    def __init__(self , maxSize):
        self.maxSize = maxSize

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
           return False

    def push(self , value):
        if self.isFull():
            return "The stack is full ."
        else:
            self.list.append(value)
            return "successfully added to stack ."
        

    def pop(self):
        if self.list == []:
            return " Stack is already empty ."
        else:
            return self.list.pop()
        
    def peek(self):
        if self.list == []:
            return 'stack is empty .'
        else:
            return self.list[-1]