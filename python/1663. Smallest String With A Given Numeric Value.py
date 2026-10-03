class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res=["a"]*n
        dif = k-n
        idx=n-1
        while dif>25:
            res[idx]="z"
            idx-=1
            dif-=25
        ch=chr(ord(res[idx])+dif)
        res[idx]=ch
        return "".join(res)
    
            
            
