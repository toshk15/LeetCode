class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        l=0
        n=len(s)
    
        while l<n:
            r=l
            while r<n and s[r]==s[l]:
                r+=1
            if k==r-l:
               return True
            l=r
        return False
