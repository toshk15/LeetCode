# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        dummy=ListNode()
        dummy.next=head
        left=dummy
        while left.next:
            right=left.next
            sumTotal=0
            while right:
                sumTotal+=right.val
                if sumTotal==0:
                    break
                right=right.next
            if sumTotal==0:
                left.next=right.next
                continue
            left=left.next
        return dummy.next
            
