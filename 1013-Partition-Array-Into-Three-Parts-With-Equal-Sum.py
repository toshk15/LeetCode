class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sumT=sum(arr)
        res=0
        result=[]
        x=sumT/3
        for i in arr:
            res+=i            
            if res==x:
                result.append(1)
                res=0
                
            if len(result)==3:
                return True
            
        return False
    
"""
Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

"""