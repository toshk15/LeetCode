class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_nodes(head):
    
    curr = head
    stack = []    

    while curr:
        while stack and curr.val > stack[-1]:
            stack.pop()
        stack.append(curr.val)
        curr = curr.next

    dummy = ListNode(0)
    curr = dummy

    for n in stack:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next
    
def printList(n):
    curr = n
    while curr:
        print(curr.val)
        curr = curr.next


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(12)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

n = remove_nodes(head)
printList(n)
