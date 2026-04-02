# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
sys.set_int_max_str_digits(0)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num=""
        curr=head
        dummy=ListNode()
        while curr:
            num+=str(curr.val)
            curr=curr.next
        num=int(num)*2
        num=str(num)
        aux=dummy
        for i in range(len(num)):
            node=ListNode(int(num[i]))
            aux.next=node
            aux = node
        return dummy.next
            
            
        
        
            
