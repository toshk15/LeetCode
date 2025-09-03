class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    """
    def preOrder(self, root):
        if root == None:
            return []
        else:
            pre = []
            stack = []
            stack.append(root)
            while stack:
                node = stack.pop()
                pre.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return pre
    """

    def preOrder(self, root):
        curr, stack = root, []
        res = []

        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res

node = Tree(1)
node.left = Tree(2)
node.right = Tree(3)
node.left.left = Tree(4)
node.right.right = Tree(5)

print(node.preOrder(node))

