class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]        

    def push(self, x: int) -> None:
        self.stack1.append(x)        

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()        

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]        

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        else:
            return True

myQueue=MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek() #return 1
myQueue.pop() #return 1, queue is [2]
myQueue.empty() #return false