def nextGreaterElement(num1, num2):
    
    numIdx = {n:i for i, n in enumerate(num1)}
    res = [-1]*len(num1)
    """
    stack=[]
    #for i in range(len(num2)):
    for curr in num2:
        #curr = num2[i]

        while stack and curr > stack[-1]:
            val = stack.pop()
            idx = numIdx[val]
            res[idx] = curr
        
        if curr in numIdx:
            stack.append(curr)

    return res

    """

    for i in range(len(num2)):
        if num2[i] not in numIdx:
            continue

        for j in range(i+1, len(num2)):
            if num2[j] > num2[i]:
                idx = numIdx[num2[i]]
                res[idx] = num2[j]
                break

    return res

num1=[4,1,2]
num2=[1,3,4,2]

print(nextGreaterElement(num1, num2))