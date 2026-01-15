# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        res_sum=[]
        s=[0]
        def treeSum(node):
            if node is None:
                return 0

            s[0]=node.val + treeSum(node.left) + treeSum(node.right)            
            res_sum.append(s[0])
            return s[0]

        total_sum=treeSum(root)
        max_sum=0
        for n in res_sum:
            max_sum=max(max_sum, n*(total_sum-n))
        return max_sum%(7+(10**9))

        
