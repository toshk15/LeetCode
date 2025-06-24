class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    
def delete(head):

    if head == None:
        return head
        
    elif head != None and head.next == None:
            return head
        
    else:
        re = {}
        curr = head
        prev = head

        while curr:
            if curr.val in re:
                prev = prev.next.next
            else:
                re[curr.val] = True
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

head = delete(head)
printLinkList(head)



        
        