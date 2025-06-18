class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularQueue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, val):
        new_node = Node(val)

        if self.front is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

    def dequeue(self):
        
        if self.front is None:
            print("queue is empty")
        elif self.front == self.rear:
            data = self.front.val
            self.front = self.rear = None
            return data
        else:
            data = self.front.val
            self.front = self.front.next
            self.rear.next = self.front
            return data

    def printCircularQueue(self):

        curr = self.front
        while True:
            print(curr.val)
            curr = curr.next
            if curr == self.front:
                break
        return

c = CircularQueue()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.printCircularQueue()
c.dequeue()
print("------------------")
c.printCircularQueue()
    

    