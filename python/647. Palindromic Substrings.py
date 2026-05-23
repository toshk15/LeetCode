class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0
        def count(s,l,r):
            res=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        for i in range(len(s)):
            c+=count(s,i,i)
            c+=count(s,i,i+1)
        return c
        
