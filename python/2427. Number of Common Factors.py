class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res=0
        while b:
            a,b=b,a%b
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                res+=1
        return res
