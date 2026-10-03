class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        p=set()
        def prime(n):
            if n<2:
                return False
            for i in range(2,int(sqrt(n)+1)):
                if n%i==0:
                    return False
            return True
        for i in range(len(s)):
            cur=0
            for j in range(i,len(s)):
                cur=cur*10+int(s[j])
                if prime(cur):
                    p.add(cur)
        res=sorted(p)
        return sum(res[-3:])
                

            
                
