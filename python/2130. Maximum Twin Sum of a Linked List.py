# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            tem=slow.next
            slow.next=prev
            prev=slow
            slow=tem
        first=head
        second=prev
        m=float("-inf")
        while second:
            m=max(m,first.val+second.val)
            first=first.next
            second=second.next
        return m
        


        
        
