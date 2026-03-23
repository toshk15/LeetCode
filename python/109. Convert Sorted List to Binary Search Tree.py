# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def binary(arr):
            if arr==[]:
                return
            m = len(arr)//2
            node = TreeNode(arr[m])
            node.left=binary(arr[:m])
            node.right=binary(arr[m+1:])
            return node
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        return binary(res)
            
