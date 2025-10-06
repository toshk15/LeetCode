def rowAndMaximumOnes(mat):
    max_ones=0
    stack=[]
    for idx, row in enumerate(mat):
        c=row.count(1)
        if c>max_ones:
            stack.append([idx,c])
            max_ones=c
    if stack:
        return stack.pop()
    else:
        return [0,0]
    
mat = [[0,0],[1,1],[0,0]]
