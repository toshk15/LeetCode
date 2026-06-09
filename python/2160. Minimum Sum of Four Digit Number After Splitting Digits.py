class Solution:
    def minimumSum(self, num: int) -> int:
        numstr=list(str(num))
        numstr.sort()
        print(numstr)
        l=0
        r=len(numstr)-1
        s=0
        while l<r:
            s+=int(numstr[l] + numstr[r])
            l+=1
            r-=1
        return s
        
