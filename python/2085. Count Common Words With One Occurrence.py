class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1=Counter(words1)
        w2=Counter(words2)
        res=0
        seen=set()
        for w in words1:
            if w not in seen:
                if w1[w]==1 and w2[w]==1:
                    res+=1
            seen.add(w)
        return res
                
