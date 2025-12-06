class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isValidBST(root):
    r=[]
    res = inOrder(root,r)      
    print(res) 
    x = res[0]

    for num in res[1:]:
        if num <= x:
            return False
        x=num
    return True

def inOrder(root,r):
    
    if not root:
        return 

    inOrder(root.left,r)
    r.append(root.val)
    inOrder(root.right,r)
    return r
    
        
root = Tree(5)
root.left = Tree(4)
root.right = Tree(6)
root.left.left = Tree(3)
root.right.right = Tree(8)

print(isValidBST(root))
