class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

        
def removeElements(head, x):

    dummy = Node(0)
    dummy.next = head
    curr = dummy

    while curr.next:
        
        if curr.next.val == x:
            curr.next = curr.next.next
        else:
            curr = curr.next      
    return dummy.next

def printList(head):
    curr = head

    while curr:
        print(curr.val)
        curr = curr.next


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(3)
node.next.next.next.next = Node(4)
printList(node)
print("---------------")
n = removeElements(node, 1)
printList(n)


