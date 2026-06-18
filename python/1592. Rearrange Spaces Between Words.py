class Solution:
    def reorderSpaces(self, text: str) -> str:
        sp=text.count(" ")
        t=text.split()
        l=len(t)
        if l==1:
           return t[0]+ " "*sp
        midsp=sp//(l-1)
        endsp=sp%(l-1)
        return (" "*midsp).join(t)+" "*endsp
            
