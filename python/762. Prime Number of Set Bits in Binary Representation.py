class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        def prime(n):
            for i in range(2,int(math.sqrt(n)+1)):
                if n%i==0:
                    return False
            return n>=2
        
        for i in range(left,right+1):
            b=bin(i)
            nb=b.count("1")
            if prime(nb):
                res+=1
        return res
