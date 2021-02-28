class Stack():
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return f'{self.stack}'

    def isEmpty(self):
        # print('self', self)
        return self.stack == []

    def push(self, input_object: str):
        self.stack.append(input_object)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)