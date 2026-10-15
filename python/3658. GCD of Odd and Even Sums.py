class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even=0
        odd=0
        for i in range(2*n+1):
            if i%2==0:
                even+=i
            else:
                odd+=1
        def GCD(a,b):
            while b:
                a,b=a,a%b
            return abs(a)
        
        return GCD(odd,even)
                
