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

"""
Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""