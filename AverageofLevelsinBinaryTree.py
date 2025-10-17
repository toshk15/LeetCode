from collections import deque
def averageOfLevels(root):
    q = deque()
    q.append(root)
    avg=[]

    while q:
        s=0
        n=len(q)
        for i in range(n):
            node = q.popleft()
            s+=node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        s/= n
        avg.append(s)
    return avg