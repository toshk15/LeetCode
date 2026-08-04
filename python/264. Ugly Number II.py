class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        idx2=0
        idx3=0
        idx5=0
        while len(ugly)<n:
            ugly2=ugly[idx2]*2
            ugly3=ugly[idx3]*3
            ugly5=ugly[idx5]*5
            mi=min(ugly2,ugly3,ugly5)
            ugly.append(mi)
            if mi==ugly2:
                idx2+=1
            if mi==ugly3:
                idx3+=1
            if mi==ugly5:
                idx5+=1
        print(ugly)
        return ugly[-1]
        
            
        
