def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    sets = set(wordDict)
    n = len(s)
    dp=[False]*(n+1)
    lmax=0
    dp[0]=True
    for w in wordDict:
        lmax=max(lmax,len(w))
       
    for i in range(1, n+1):
        for j in range(i-1, max(0,i-lmax)-1, -1):
            if dp[j] and s[j:i] in sets:
                dp[i]=True
                break
    return dp[n]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]