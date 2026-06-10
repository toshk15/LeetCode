class Solution:
    def maxProduct(self, n: int) -> int:
        num=list(str(n))
        num.sort()
        print(num)
        pmax=0
        for i in range(len(num)-1):
            pmax=max(pmax,int(num[i])*int(num[i+1]))
        return pmax
