class Solution:
    
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        import sys
        sys.set_int_max_str_digits(0)
        r=[]
        num="".join(map(str,num))
        num=int(num)
        res = num+k
        res = str(res)
        for i in res:
            r.append(int(i))
        return r
    
"""
Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
"""