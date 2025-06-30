class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [None] * k
        self.front = self.rear = -1
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    
    def isEmpty(self):
        return self.front == -1
    
    def enqueue(self, val):
        if self.isFull():
            raise IndexError("enqueue on a full queue")
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = val

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("queue is empty")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
        return item
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from an empty queue")
        return self.queue[self.front]
    
    def sizeL(self):
        if self.isEmpty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.size - self.front + self.rear + 1

c = CircularQueue(5)
c.enqueue(1)
c.enqueue(2)
#c.enqueue(3)
#c.enqueue(4)
#c.enqueue(5)

#c.enqueue(6)
print(c.dequeue())
print(c.dequeue())
#print(c.dequeue())
#c.enqueue(5)
#print(c.peek())
print(c.sizeL())



        