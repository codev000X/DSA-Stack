class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        
        values = [str(x) for x in reversed(self.list)]
        return "/n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.list == []:
            return "List is empty ."
        else:
            self.list.pop()

    def peek(self):
        if self.list == []:
            return "List is empty ."
        else:
            return self.list[-1]
        
    def delete(self):
        return self.list == None

    def push(self , value):
        self.list.append(value)
        return "Element succesfully added ."