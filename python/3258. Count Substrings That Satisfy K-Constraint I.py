class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res=0
        z=0
        o=0
        l=0
        for r in range(len(s)):
            if s[r] == "0":
                z+=1
            else:
                o+=1
            while z>k and o>k:
                if s[l]=="0":
                    z-=1
                else:
                    o-=1
                l+=1
            res+=r-l+1
        return res
