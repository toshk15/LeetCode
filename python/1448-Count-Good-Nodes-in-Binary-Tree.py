def goodNodes(root):
    goods = 0
    stack = [root]
    largest=[float("-inf")]

    while stack:
        node = stack.pop()
        l = largest.pop()

        if node.val >= l:
            goods+=1

        l= max(l, node.val)

        if node.left:
            stack.append(node.left)
            largest.append(l)

        if node.right:
            stack.append(node.right)
            largest.append(l)
    return goods

"""
Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""