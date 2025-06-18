class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, root, key):

        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        return root

    def preorder(self, root):

        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
        return

root = Node(5)
root = root.insert(root, 1)
root = root.insert(root, 8)

root.preorder(root)

