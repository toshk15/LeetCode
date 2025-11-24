# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        s=set()
        def dfs(root):
            if not root:
                return None
            if not root.val in s:
                s.add(root.val)

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return True if len(s)==1 else False
    
"""
Example 1:

Input: root = [1,1,1,1,1,null,1]
Output: true

Example 2:

Input: root = [2,2,2,5,2]
Output: false

"""