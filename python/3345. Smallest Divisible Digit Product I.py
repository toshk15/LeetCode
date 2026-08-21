class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            num=n
            p=1
            while num:
                d=num%10
                p=p*d
                num=num//10
            if p%t==0:
                return n
            n+=1
