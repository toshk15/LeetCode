class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse1=int(str(num)[::-1])
        reverse2=int(str(reverse1)[::-1])
        return num==reverse2
        
