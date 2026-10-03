class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans=0
        if n&k!=k:
            return -1
        res=n^k
        b=""
        while res:
            b=str(res%2)+b
            res//=2
            
        for i in b:
            if i=="1":
                ans+=1
        return ans
