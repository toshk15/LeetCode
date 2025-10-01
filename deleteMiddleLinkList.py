
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    if not head:
        return None
    if head and not head.next:
        return None

    low = head
    fast = head
    mid = low
    while fast and fast.next:
        mid = low
        low = low.next
        fast = fast.next.next
        
    mid.next = mid.next.next
    return head