# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([(root, None)])
        while q:
            xx=None
            yy=None
            for i in range(len(q)):
                node,parent=q.popleft()
                if node.val==x:
                    xx=parent
                if node.val==y:
                    yy=parent
                if node.left:
                    q.append((node.left,node))
                if node.right:
                        q.append((node.right,node))
            if xx or yy:
                return xx is not None and yy is not None and xx!=yy
                        
        
