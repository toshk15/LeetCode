class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:
            return True
        def reverse(n):
            num=0
            while n:
                num=num*10+(n%10)
                n//=10
            return num
        for i in range(num):
            rev=reverse(i)
            if rev+i==num:
                return True
        return False
