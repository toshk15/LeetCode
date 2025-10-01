class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    d = {}
    stack=[(root, False)]
    diameter=0
        
    while stack:
        node, visited =stack.pop()

        if visited:
            left = d.get(node.left,0)
            right= d.get(node.right,0)
            diameter = max(diameter, left+right)
            d[node]=1+max(left,right)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))            
    return diameter
        
root = Tree(5)
root.left = Tree(4)
root.right = Tree(6)
root.left.left = Tree(3)
root.right.right = Tree(8)

print(diameterOfBinaryTree(root))