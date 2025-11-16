class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    """
    def removeElements(self,head, val):
        prev = curr = head

        while curr:
            #aux = curr.next
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head
    """
    def removeElements(self, head, val):
        dummy = Node(0,head)
        prev = dummy
        curr = head

        while curr:
            if curr.val != val:
                prev = curr
                curr=curr.next
            else:
                prev.next = curr.next 
                curr = curr.next
        return dummy.next   
    
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

head.removeElements(head, 3)
head.printLinkList(head)

