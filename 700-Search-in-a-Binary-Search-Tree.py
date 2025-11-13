class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return root
        
        if root.val == val: 
            return root        
        
        if root.val<val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        
        
"""
Example1:   
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example2:
Input: root = [4,2,7,1,3], val = 5
Output: []
"""