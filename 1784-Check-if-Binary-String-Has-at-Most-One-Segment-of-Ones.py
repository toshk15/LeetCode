class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n=len(s)
        c=0    
        res=[]  
        for i in s:
            if i=="1":
                c+=1                                                       
            elif i=="0":
                if c>=1:
                    res.append(c)
                    c=0
                else:
                    continue
        if c:
            res.append(c)
        if len(res)>1:
            return False
        else:
            return True
        
"""
Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.

Example 2:

Input: s = "110"
Output: true
"""