# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res=[]
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        l,r=0,len(res)-1
        while l<r:
            s=res[l]+res[r]
            if s==k:
                return True
            elif s>k:
                r-=1
            else:
                l+=1
        return False
        
        
