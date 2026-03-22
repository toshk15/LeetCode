# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        curr=head
        while curr:
            res.append(curr.val)
            curr=curr.next
        res.sort()
        temp=head
        i=0
        while temp:
            temp.val=res[i]
            i+=1
            temp=temp.next
        return head
