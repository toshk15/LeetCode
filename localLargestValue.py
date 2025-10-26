def largestLocal(arr):
    N = len(arr)
    res = [[0]*(N-2) for x in range(N-2)]

    for i in range(N-2):
        for j in range(N-2):
            for r in range(i, i+3):
                for c in range(j, j+3):
                    res[i][j] = max(res[i][j], arr[r][c])
    return res

arr = [[1,2,3,4,5],[3,5,3,2,1],[1,1,1,1,1],[0,8,7,6,0]]
print(largestLocal(arr))

