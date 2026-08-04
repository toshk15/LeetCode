class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d={}
        diff=0
        for i in range(len(s)):
            d[s[i]]=i
        for j in range(len(t)):
            diff+=abs(d[t[j]]-j)
        return diff
