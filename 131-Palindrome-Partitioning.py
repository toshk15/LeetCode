class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part=[]
        res=[]

        def pali(s,i,x):
            while i<=x:
                if s[i]!=s[x]:
                    return False
                i+=1
                x-=1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            
            for x in range(i, len(s)):
                if pali(s,i,x):
                    part.append(s[i:x+1])
                    dfs(x+1)
                    part.pop()
        dfs(0)
        return res

"""

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

"""