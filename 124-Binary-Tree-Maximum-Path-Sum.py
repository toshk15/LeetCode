# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sumP = [root.val]

        def sumPath(root):
            if not root:
                return 0

            leftSum=sumPath(root.left)
            rightSum=sumPath(root.right)
            leftSumMax=max(leftSum,0)
            rightSumMax=max(rightSum,0)
            sumP[0]=max(sumP[0],root.val+leftSumMax+rightSumMax)

            return root.val + max(leftSumMax, rightSumMax)
        sumPath(root)
        return sumP[0]
    
"""
Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

"""