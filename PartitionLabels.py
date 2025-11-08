class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c={}
        res=[]
        size=0
        m=0
        for i, j in enumerate(s):
            c[j]=i
        
        for i in range(len(s)):
            size+=1
            end=c[s[i]]
            m = max(m,end)
            if m==i:
                res.append(size)
                size=0
        return res
    

"""
Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

"""