class Solution:
    def countValidWords(self, sentence: str) -> int:
        words=sentence.split()
        
        res=0
        for w in words:
            hyphen=0
            flag=True
            for i,ch in enumerate(w):
                if ch.isdigit():
                    flag=False
                elif ch =='-':
                    hyphen+=1
                    if hyphen>1:
                        flag=False
                    if i==0 or i==len(w)-1:
                        flag=False
                    else:
                        if not (w[i-1].isalpha() and w[i+1].isalpha()):
                            flag=False
                if ch in ".,!":
                    if i!=len(w)-1:
                        flag=False
            if flag:
                res+=1
        return res
                    
                    
