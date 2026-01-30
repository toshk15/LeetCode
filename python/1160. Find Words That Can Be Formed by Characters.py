class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res=0
        c=Counter(chars)
        for w in words:
            ch=Counter(w)
            cnt=0
            for char,count in ch.items():
                if count<=c[char]:
                    cnt+=1
                else:
                    break
            if cnt==len(ch):
                res+=len(w)
        return res
                    
