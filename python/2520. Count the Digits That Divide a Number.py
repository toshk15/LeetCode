class Solution:
    def countDigits(self, num: int) -> int:
        res=0
        s=str(num)
        for i in range(len(s)):
            if num%int(s[i])==0:
                res+=1
        return res
    
