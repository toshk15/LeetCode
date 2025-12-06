class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class circularQueue:
    def __init__(self, size):
        self.size = size
        self.left = Node(0, None, None)
        self.right = Node(0, None, self.left)
        #self.left.next = self.right

    def enqueue(self, value):
        if self.isFull(): return False
        curr = Node(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.size -= 1
        return True
    
    def dequeue(self):
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size += 1
        return True
    
    def isEmpty(self):
        return self.left.next == self.right
    
    def isFull(self):
        return self.size == 0
    
    def front(self):
        if self.isEmpty(): return -1
        return self.left.next.val
    
    def rear(self):
        if self.isEmpty(): return -1
        return self.right.prev.val
    
    def printQueue(self):
        curr = self.left
        while curr:
            print(curr.val)
            curr = curr.next

    
node = circularQueue(3)
node.enqueue(1)
node.enqueue(1)
node.enqueue(1)
node.dequeue()
node.printQueue()
    

        
        