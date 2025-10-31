class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: 

        l=ListNode()
        r=ListNode()      

        ltail=l
        rtail=r

        ptr = head

        while ptr:
            if ptr.val < x:
                ltail.next=ptr
                ltail=ltail.next
            else:
                rtail.next=ptr
                rtail=rtail.next
            ptr=ptr.next

        ltail.next=r.next
        rtail.next=None
        
        return l.next
"""
  
Example 1:
     
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""  