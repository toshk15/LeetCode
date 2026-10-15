class Solution:
    def rotatedDigits(self, n: int) -> int:
        res=0
        r ={"0":"0","1":"1","8":"8","2":"5","5":"2","6":"9","9":"6"}
        for i in range(1,n+1):
            s=str(i)
            ns=""
            for c in s:
                if c in r:
                    ns+=r[c]
                else:
                    break
            if len(s)==len(ns) and ns!=s:
                res+=1
        return res
