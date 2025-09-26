class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

""" 
def deleteDuplicates(head):

    if head == None:
        return head
        
    elif head != None and head.next == None:
            return head
        
    else:
        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
"""   

"""
def deleteDuplicates(head):

    if not head:
        return None
    ptr1 = head
    ptr2 = head.next  

    while ptr2:            
        if ptr1.val == ptr2.val:
            if not ptr2.next:
                ptr1.next = None
            ptr2 = ptr2.next
        else:
            ptr1.next = ptr2
            ptr1 = ptr2
            ptr2 = ptr2.next
    return head

"""

def deleteDuplicates(head):
    if head == None:
        return head
    elif head != None and head.next == None:
        return head
    else:
        c = {}
        prev = head
        curr = head
        while curr != None:
            if curr.val in c:
                prev.next = prev.next.next
            else:
                c[curr.val] = True
                prev = curr
            curr = curr.next
        return head    
    
    
def printLinkList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)

head1 = deleteDuplicates(head)
printLinkList(head1)



        
        