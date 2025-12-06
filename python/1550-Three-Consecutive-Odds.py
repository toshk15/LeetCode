class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c=0
        for n in arr:
            if n%2==1:
                c+=1
                if c==3:
                    return True
            else:
                c=0
        return False
    
"""
Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
"""