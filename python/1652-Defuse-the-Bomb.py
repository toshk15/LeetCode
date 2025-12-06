class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        l=0
        currSum=0

        for r in range(n+abs(k)):
            currSum+=code[r%n]

            if r-l+1>abs(k):
                currSum-=code[l%n]
                l=(l+1)%n
            if r-l+1==abs(k):
                if k>0:
                    res[(l-1)%n]=currSum
                if k<0:
                    res[(r+1)%n]=currSum
        
        return res
    
"""
Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 

Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

"""