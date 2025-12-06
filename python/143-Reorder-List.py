# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
       
        slow=head
        fast=head

        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next

        second=slow.next
        slow.next = None

        prev=None
        ptr=second

        while ptr:
            aux=ptr.next
            ptr.next=prev
            prev=ptr
            ptr=aux

        curr = head
        se=prev
        dummy=ListNode()
        join=dummy

        while curr and se:
            join.next=curr
            join = curr
            curr=curr.next
            join.next=se
            join=se
            se=se.next
            
        if curr:
            join.next=curr
        if se:
            join,next=se
        return dummy.next

"""
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""