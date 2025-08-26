class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
    
    old_head = head

    curr, size = head, 0
    while curr:
        curr, size = curr.next, size + 1

    if k % size == 0:
        return head
    
    k %= size
    slow = fast = head
    while fast and fast.next:
        if k <= 0:
            slow = slow.next
        fast = fast.next
        k -= 1
    
    new_tail, new_head, old_tail = slow, slow.next, fast
    new_tail.next, old_tail.next = None, old_head

    return new_head

def printLinkList(head):

    curr = head

    while curr:
        print(curr.data)
        curr = curr.next



node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = Node(6)
r = rotateRight(node, 2)

printLinkList(r)


    

