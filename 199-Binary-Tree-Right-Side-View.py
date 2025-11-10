from collections import deque
def rightSideView(root):
    q = deque()
    q.append(root)
    res=[]
    value=0
    if not root:
        return []

    while q:
        size = len(q)
        for u in range(size):
            node = q.popleft()
            value = node.val              

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(value)
    return res