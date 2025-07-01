class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kthSmallestbst(root, k):
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        k -= 1
        
        if k == 0:
            return curr.val
        curr = curr.right

node = Node(5)
node.left = Node(4)
node.right = Node(6)
node.left.left = Node(3)
node.left.right = Node(4)
node.right.right = Node(7)

print(kthSmallestbst(node, 3))



    