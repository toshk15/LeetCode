# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minimum=[float("inf")]
        prevNode=[None]

        def dfs(root):

            if not root:
                return

            dfs(root.left)

            if prevNode[0] is not None:
                minimum[0] = min(minimum[0], abs(root.val-prevNode[0]))
            prevNode[0]=root.val
           
            dfs(root.right)

        dfs(root)
        return minimum[0]
    

"""
Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

"""