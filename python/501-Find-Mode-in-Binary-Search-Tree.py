# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        #m=float("-inf")
        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)         

        dfs(root)
        c=Counter(res)
        maxVal=max(c.values())
        m = [key for key, value in c.items() if value == maxVal]

        return m

"""   
Example 1:

Input: root = [1,null,2,2]
Output: [2]

Example 2:

Input: root = [0]
Output: [0]
""" 