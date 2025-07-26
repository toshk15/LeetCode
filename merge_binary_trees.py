class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def merge_tress(root1, root2):
     
     if not root1:
         return root2
     
     if not root2:
         return root1
     
     merge_node = Tree(root1.val + root2.val)

     merge_node.left = merge_tress(root1.left, root2.left)
     merge_node.right = merge_tress(root1.right, root2.right)

     return merge_node

def preorder(root):
    if not root:
        return None
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)


root1 = Tree(3)
root1.right = Tree(4)
root1.left = Tree(2)

root2 = Tree(3)
root2.right = Tree(4)
root2.left = Tree(2)

root = merge_tress(root1, root2)
preorder(root)