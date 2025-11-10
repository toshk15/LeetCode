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


"""
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]


"""