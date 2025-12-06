# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        s=""
        def dfs(root,s):
            if not root:
                return

            if s:
                s += "->" + str(root.val)
            else:
                s = str(root.val)

            if not root.left and not root.right:
                res.append(s)
                return           

            dfs(root.left,s)
            dfs(root.right,s)
        dfs(root,s)
        print(res)
        return res
    
"""
Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:

Input: root = [1]
Output: ["1"]

"""