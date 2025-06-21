class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def removeElement(self,head, val):
        prev = curr = head

        while curr:
            #aux = curr.next
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head
    
    def printLinkList(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

        
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(3)

head.removeElement(head, 3)
head.printLinkList(head)

