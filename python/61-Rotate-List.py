class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        size=0
        pasthead=head
        curr=head
        while curr:
            size+=1
            curr=curr.next
        k=k%size
        if k==0:
            return head
            
        slow=head
        fast=head

        while fast and fast.next:
            
            if k<=0:
                slow=slow.next
            fast=fast.next
            k-=1
        
        newhead=slow.next
        newtail=slow
        newtail.next=None
        fast.next = pasthead
        return newhead
    
"""
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

"""

