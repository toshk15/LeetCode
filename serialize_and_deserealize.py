class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root):
    res = []
    def dfs(node):
        if not node:
            res.append("N")
            return
        
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    r = ",".join(res)
    return r

def deserialize(data):
    s = data.split(",")
    def dfs():
        n = s.pop(0)
        
        if n == "N":
            return None
        
        node = Tree(int(n))
        node.left = dfs()
        node.right = dfs()

        return node
    return dfs()

def preorder(root):

    if not root:
        return None
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)



root = Tree(5)
root.left = Tree(4)
root.right = Tree(6)

ser = serialize(root)
print(ser)

no = deserialize(ser)
preorder(no)