class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res=[]
        w1=len(word1)
        w2=len(word2)
        i=0
        j=0
        while i<w1 and j<w2:
            if word1[i:]>word2[j:]:
                res.append(word1[i])
                i+=1
            else:
                res.append(word2[j])
                j+=1
        if i<w1:
            res.append(word1[i:])
        if j<w2:
            res.append(word2[j:])
        return "".join(res)
