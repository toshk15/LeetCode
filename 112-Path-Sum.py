class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    """
    def pathSum(self, root, targetSum):
        
        def dfs(node, currSum):
            if not node:
                return False
        
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            
            return (dfs(node.left, currSum) or dfs(node.right, currSum))
        
        return dfs(root, 0)
        """
def pathSum(root, targetSum):
    if not root:
        return False
        
    st_sum=[]
    st_path=[]
    st_sum.append(root.val)
    st_path.append(root)

    while st_path:
        node = st_path.pop()
        val = st_sum.pop()

        if not node.left and not node.right and val == targetSum:
            return True
            
        if node.right:                
            st_path.append(node.right)
            st_sum.append(node.right.val + val)
        if node.left:                
            st_path.append(node.left)
            st_sum.append(node.left.val + val)

    return False

node = Tree(1)
node.left = Tree(2)
node.right = Tree(7)
node.left.left = Tree(4)
node.left.right = Tree(5)
node.right.left = Tree(3)
node.right.right = Tree(9)

print(pathSum(node, 11))


         