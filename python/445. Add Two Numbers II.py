# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        s1=""
        s2=""
        while cur1:
            s1+=str(cur1.val)
            cur1=cur1.next
        while cur2:
            s2+=str(cur2.val)
            cur2=cur2.next
        s=int(s1)+int(s2)
        s=str(s)
        dummy=ListNode()
        aux=dummy
        for n in range(len(s)):
            node = ListNode(int(s[n]))
            aux.next = node
            aux = node
        return dummy.next
            
            
