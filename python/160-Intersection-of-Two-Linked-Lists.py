
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return 0

    s = set()
    currA=headA
    currB=headB

    while currA:
        s.add(currA)
        currA=currA.next

    while currB:
        if currB in s:
            return currB.val
        currB=currB.next   

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(5)


l2 = Node(3)
l2.next = l1.next.next
l2.next.next = Node(6)
l2.next.next.next = Node(8)
l2.next.next.next.next = Node(9)
print(getIntersectionNode(l1, l2))  
