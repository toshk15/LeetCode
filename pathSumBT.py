class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def pathSum(self, root, targetSum):
        
        def dfs(node, currSum):
            if not node:
                return False
        
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            
            return (dfs(node.left, currSum) or dfs(node.right, currSum))
        
        return dfs(root, 0)
    
node = Tree(1)
node.left = Tree(2)
node.right = Tree(7)
node.left.left = Tree(4)
node.left.right = Tree(5)
node.right.left = Tree(3)
node.right.right = Tree(9)

print(node.pathSum(node, 11))


         