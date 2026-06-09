class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower={}
        upper={}
        res=0
        for i,c in enumerate(word):
            if c.islower():
                lower[c]=i
            elif not c in upper:
                upper[c]=i
        for i in range(26):
            c=chr(ord('a')+i)
            if c in lower and c.upper() in upper and lower[c]<upper[c.upper()]:
                res+=1
        return res
                
