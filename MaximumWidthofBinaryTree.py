from collections import deque
def widthOfBinaryTree(root):
    if not root:
        return 0
    width=0
    q=deque([root])
    index=deque([0])

    while q:
        n = len(q)
        l = index[0]
        r=l
        for x in range(n):
            node = q.popleft()
            i=index.popleft()

            if node.left:
                q.append(node.left)
                index.append(2*i+1)
            if node.right:
                q.append(node.right)
                index.append(2*i+2)
            r=i
        width=max(width, r-l+1)
    return width