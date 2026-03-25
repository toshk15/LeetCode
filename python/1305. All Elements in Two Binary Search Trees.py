# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        res=[]
        def inorder(root,res):
            if not root:
                return
            res.append(root.val)
            inorder(root.left,res)
            inorder(root.right,res)
        inorder(root1,res)
        inorder(root2,res)
        res.sort()
        return res
