class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res=[words[0]]
        x=groups[0]
        n=len(groups)
        for i in range(1,n):
            if x!=groups[i]:
                res.append(words[i])
            x=groups[i]
        return res
        
