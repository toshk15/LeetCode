from collections import defaultdict

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def duplicates_subtrees(root):
    subtress = defaultdict(list)

    def dfs(node):
        if not node:
            return "null"
        s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
        if len(subtress[s]) == 1:
            res.append(node)
        subtress[s].append(node)
        return s
    res = []
    dfs(root)
    return res

root = Tree(1)
root.left = Tree(2)
root.left.left = Tree(4)
root.right = Tree(3)
root.right.right = Tree(4)
root.right.left = Tree(2)
root.right.left.left = Tree(4)


print(duplicates_subtrees(root))


    