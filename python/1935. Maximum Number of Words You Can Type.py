class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        res=0
        broken=set(brokenLetters)
        for w in text:
            flag=True
            for c in w:
                if c in broken:
                    flag=False
                    break
            if flag:
                res+=1
                    
        return res
