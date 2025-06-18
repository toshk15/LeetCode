class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class CircularLinkList:
    def __init__(self):
        self.head = None

    def enqueue(self, val):

        curr = self.head

        new_node = Node(val)

        if self.head == None:
            new_node.next = new_node
            self.head = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            
            curr.next = new_node
            new_node.next = self.head

    def printLinkList(self):

        curr = self.head
        while True:
            print(curr.val)
            curr = curr.next

            if curr == self.head:
                break
    
circularList = CircularLinkList()
circularList.enqueue(1)
circularList.enqueue(2)
circularList.enqueue(3)
circularList.printLinkList()
