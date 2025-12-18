# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafs(root,res):
            if not root:
                return

            if not root.left and not root.right:
                res.append(root.val)

            getLeafs(root.left,res)
            getLeafs(root.right,res)
        l1=[]
        l2=[]
        getLeafs(root1, l1)
        getLeafs(root2, l2)

        return l1==l2
    

"""
Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

"""