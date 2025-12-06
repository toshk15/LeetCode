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

"""
Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:

Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:

Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
"""