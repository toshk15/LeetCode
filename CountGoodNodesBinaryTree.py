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