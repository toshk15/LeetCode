class Solution:
    def equalFrequency(self, word: str) -> bool:
        c=Counter(word)
        k=list(c.keys())
        for key in k:
            c[key]-=1
            if c[key]==0:
                del c[key]
            s=len(set(c.values()))
            if s==1:
                return True
            c[key]+=1
        return False
            
