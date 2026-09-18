# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        prev=head
        cur=head.next
        while cur:
            g=gcd(prev.val,cur.val)
            node=ListNode(g)
            prev.next=node
            node.next=cur
            prev=cur
            cur=cur.next
        return head
            
