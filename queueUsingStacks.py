class queue:

    def __init__(self):
        self.stack = []
        self.invStack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.invStack:
            while self.stack:
                self.invStack.append(self.stack.pop())
        return self.invStack.pop()
    
    def peek(self):
        if not self.invStack:
            while self.stack:
                self.invStack.append(self.stack.pop())
        return self.invStack[-1]
    
    def empty(self):
        return not(self.stack or self.invStack)
    
q = queue()

q.push(1)
q.push(2)
q.push(3)

print(q.pop())
print(q.pop())
print(q.pop())

print(q.empty())

