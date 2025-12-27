# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        q=deque()
        q.append(root)
        res=[]
        while q:
            s=0
            for i in range(len(q)):
                node=q.popleft()
                s+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(s)
        res.sort(reverse=True)
        return -1 if k>len(res) else res[k-1]
                    
        
