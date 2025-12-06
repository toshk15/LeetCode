def temperatures(t):
    stack=[]
    n = len(t)
    res = [0] * n

    for i in range(n-1,-1,-1):
        while stack and t[i]>=t[stack[-1]]:
            stack.pop()
        
        if stack:
            res[i]=stack[-1]-i
        stack.append(i)
    return res
temp = [73,74,75,71,69,72,76,73]
print(temperatures(temp))
