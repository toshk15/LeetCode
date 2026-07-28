class Solution:
    def minimumPushes(self, word: str) -> int:
        le=[0]*26
        res=0
        ans=0
        idx=0
        for i in range(len(word)):
            le[ord(word[i])-ord("a")]+=1
        le.sort(reverse="True")
        for i in range(len(le)):
            if le[i]>0:
                ans+=le[i]*(1+idx//8)
                idx+=1
        return ans
