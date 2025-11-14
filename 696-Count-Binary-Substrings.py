class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res=[]
        c=0
        d=0
        for i in s:
            if i=="0":
                if d>=1:
                    res.append(d)
                    d=0
                c+=1
            elif i=="1":
                if c>=1:
                    res.append(c)
                    c=0
                d+=1
        if c:
            res.append(c)
        if d:
            res.append(d)
        r=[]
        for i in range(1,len(res)):
            x=min(res[i],res[i-1])
            r.append(x)
        return sum(r)
                
"""
Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

"""