class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kthSmallestbst(root, k):
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        k -= 1
        
        if k == 0:
            return curr.val
        curr = curr.right

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [k]

        def inorder(node):
            if node is None:
                return 

            inorder(node.left)
            counter.append(node.val)
            inorder(node.right)
        inorder(root)
        return counter[k]

"""

node = Node(5)
node.left = Node(4)
node.right = Node(6)
node.left.left = Node(3)
node.left.right = Node(4)
node.right.right = Node(7)

print(kthSmallestbst(node, 3))



    