from collections import deque

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def right_nodes_tree(root):
    if not root:
        return []
    
    res = []
    queue = deque([root])

    while queue:
        len_queue = len(queue)

        for i in range(len_queue):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if i == len_queue - 1:
                res.append(node.val)
    return res


root = Tree(5)
root.left = Tree(4)
root.right = Tree(6)
root.left.left = Tree(3)
root.right.right = Tree(8)

print(right_nodes_tree(root))

