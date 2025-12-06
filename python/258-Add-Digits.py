class Solution:
    def addDigits(self, num: int) -> int:
        su=0
        n = str(num)
        if len(n)==1:
            return num

        while len(n)!=1:
            su=0                    
            i=0            
            while i<len(n):
                su+=int(n[i])
                i+=1
            n=str(su)                
        return su


"""
Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

"""