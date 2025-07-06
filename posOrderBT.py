class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def PosOrder(root):
  
    res = []
    stack = [root]
    visited = [False]

    while stack:
        curr, v = stack.pop(), visited.pop()
        if curr:
            if v:
                res.append(curr.val)                
            else:
                stack.append(curr)
                visited.append(True)
                stack.append(curr.right)
                visited.append(False)
                stack.append(curr.left)
                visited.append(False)
    
    return res


root = Tree(5)
root.left = Tree(3)
root.right = Tree(7)
root.left.right = Tree(4)
root.right.right = Tree(9)

print(PosOrder(root))
        