class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def middleNode(head):
    if not head:
        return None
        
    if head and not head.next:
        return head
        
    low = head
    fast = head
    aux = ListNode(0,head)

    while fast and fast.next:
        low = low.next
        fast = fast.next.next
        
    aux.next = low
    return aux.next