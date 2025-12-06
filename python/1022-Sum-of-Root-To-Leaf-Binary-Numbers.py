# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res=""
        c=[]
        def dfsPre(root,res):
            if not root:
                return None
            res+=str(root.val)
            if not root.left and not root.right:
                c.append(res)
            dfsPre(root.left,res)
            dfsPre(root.right,res)
        dfsPre(root,res)
        total=0
        for n in c:
            total+=int(n,2)

        return total
    

"""
Example 1:

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:

Input: root = [0]
Output: 0

"""