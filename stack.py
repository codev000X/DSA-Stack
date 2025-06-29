class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list.reverse()]
        return "/n".join(values)