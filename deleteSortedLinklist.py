from collections import Counter
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteDuplicates(head):
        curr = head
        d = []
        ci=[]
        
        while curr:
             d.append(curr.val)
             curr = curr.next

        c = Counter(d)
        

        for i in c:
             if c[i] == 1:
                  ci.append(i)          
            

        if len(ci)==0:
            return None        
     
        curr = head
        ptr = curr
        d_sort = sorted(ci)
        for i in d_sort:
            if len(d_sort) == 1:
                curr.val = i
                curr.next = None
            curr.val = i
            ptr = curr
            curr = curr.next
        ptr.next = None
        return head

def printMerge(curr):
    c = curr
    while c:
        print(c.val)
        c = c.next

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(2)
l1.next.next.next = Node(2)
l1.next.next.next.next = Node(3)
l1.next.next.next.next.next = Node(4)
l1.next.next.next.next.next.next = Node(4)
l1.next.next.next.next.next.next.next = Node(5)
s = deleteDuplicates(l1)
printMerge(s)


