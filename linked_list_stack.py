class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
    
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):  
        if not self.LinkedList.head:
            return True
        return False

    def push(self , value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head.next = node

    def pop(self):
        if not self.LinkedList.head:
            return 'Empty stack.'
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if not self.LinkedList.head:
            return 'Empty stack.'
        else:
            return self.LinkedList.head.value
    
    def delete(self):
        self.LinkedList.head = None
        