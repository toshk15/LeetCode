class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=head
        prev=dummy
        s=set(nums)

        while curr:
            if curr.val in s: 
                if curr.next==None:
                    prev.next=None
                curr = curr.next
            else:
                prev.next = curr  
                prev=curr 
                curr = curr.next            
            
        return dummy.next
    
"""
Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]
"""