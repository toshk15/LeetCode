class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def inOrder(self,root):
        if root == None:
            return []
        else:
            re = []
            stack = []
            node = root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    re.append(node.val)
                    node = node.right
            return re
        
node = Tree(1)
node.left = Tree(2)
node.right = Tree(3)
node.right.right = Tree(5)
node.left.left = Tree(4)

print(node.inOrder(node))
    