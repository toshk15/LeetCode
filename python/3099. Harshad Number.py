class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n=str(x)
        s=0
        for i in range(len(n)):
            s+=int(n[i])
        if x%s==0:
            return s
        else:
            return -1
