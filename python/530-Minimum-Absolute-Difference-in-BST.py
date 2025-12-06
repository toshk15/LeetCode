def getMinimumDifference(root):
    d = [float("inf")]
    prev = [None]

    def inorder(root):
        if root is None:
            return
            
        inorder(root.left)
        if prev[0] is not None:
            d[0]=min(d[0], root.val-prev[0])
            
        prev[0] = root.val

        inorder(root.right)

    inorder(root)
    return d[0]


"""
Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

"""  