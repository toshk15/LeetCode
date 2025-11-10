# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        s=0        
        while q:
            res=[]
            for i in range(len(q)):
                node= q.popleft()               

                if node.left:
                    q.append(node.left)  
                    if not node.left.left and not node.left.right:
                        res.append(node.left.val)                                              

                if node.right:
                    q.append(node.right)
            s+=sum(res)
        return s
    
"""
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0
"""   