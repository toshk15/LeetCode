class Solution:
    def isPrefixOfWord(self, s: str, p: str) -> int:
        s=s.split(" ")
        res=0
        for r in s:
            l=0
            res+=1
            for i in range(len(r)):
                if r[i]==p[i]:
                    l+=1
                    if len(p)==l:
                        return res
                else:
                    break
        return -1
                    
