
"""
def longesCommonSub(str1, str2):
    
    dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[0][0]
"""
"""
def longesCommonSub(str1, str2):
    n=len(str1)
    m=len(str2)

    dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j + 1], dp[i + 1][j])
    print(dp)
    return dp[m-1][n-1]
"""
def longesCommonSub(str1, str2):
    n=len(str1)
    m=len(str2)

    dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp)
    return dp[n][m]

str1 = "sad"
str2 = "ssad"
print(longesCommonSub(str1, str2))
