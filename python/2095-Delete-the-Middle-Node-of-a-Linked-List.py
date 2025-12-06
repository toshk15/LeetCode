
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


"""
Example 1:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:

Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

"""