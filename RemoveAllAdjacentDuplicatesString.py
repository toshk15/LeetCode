from collections import Counter
def removeDuplicates(s):
    """
    stack=[]
    t=""
    for i in s:
        if stack and stack[-1][0]==i:
            stack[-1][1]+=1
        if stack and stack[-1][1]==2:
            stack.pop()
            continue
        if i not in stack:
            stack.append([i,1])
        print(stack)
    for i, j in stack:
        t+=i*j
    return t    
    """
def removeDuplicates(s):
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)
#s="abbaca"
s="azxxzy"
print(removeDuplicates(s))