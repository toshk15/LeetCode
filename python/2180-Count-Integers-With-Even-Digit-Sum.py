class Solution:
    def countEven(self, num: int) -> int:        
        st=0
        for n in range(1,num+1):
            nstr = str(n)
            s=0
            for i in nstr:
                s+=int(i)
            if s%2==0:
                st+=1
        return st
            
"""
Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    

Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

"""