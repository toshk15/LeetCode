class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

"""
def isPalindrome(head):
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

def printLinkList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
"""
"""
def isPalindrome(head):

    s, f = head, head
    stack = []

    while f and f.next:
        stack.append(s.val)
        s = s.next
        f = f.next.next

    if f != None:
        s = s.next


    while s:
        x = stack.pop()
        if s.val != x:
            return False
        else:
            s = s.next
    return True

"""
def isPalindrome(head):
    elements = []

    while head:
        elements.append(head.val)
        head = head.next
        
    first, last = 0, len(elements) -1

    while first < last:
        if elements[first] == elements[last]:
            first+=1
            last-=1
        else:
            return False
    return True

head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
#head.next.next.next = Node(4)
#head.next.next.next.next = Node(3)
#head.next.next.next.next.next = Node(2)
#head.next.next.next.next.next.next = Node(1)

print(isPalindrome(head))



    
