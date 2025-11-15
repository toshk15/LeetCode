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


"""
Example 1:

Input: mat = [[0,1],[1,0]]
Output: [0,1]
Explanation: Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1). So, the answer is [0,1]. 

Example 2:

Input: mat = [[0,0,0],[0,1,1]]
Output: [1,2]
Explanation: The row indexed 1 has the maximum count of ones (2). So we return its index, 1, and the count. So, the answer is [1,2].

Example 3:

Input: mat = [[0,0],[1,1],[0,0]]
Output: [1,2]
Explanation: The row indexed 1 has the maximum count of ones (2). So the answer is [1,2].

"""