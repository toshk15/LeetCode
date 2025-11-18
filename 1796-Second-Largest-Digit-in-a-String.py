class Solution:
    def secondHighest(self, s: str) -> int:
        res=set()
        for i in s:
            if i.isnumeric():                
                res.add(int(i))
        res = sorted(list(res))
        if len(res)==1:
             return -1
        elif not res:
            return -1
        else:
            return res[-2]
        
"""
Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
"""