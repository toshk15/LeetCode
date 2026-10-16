class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ls = list(s)
        i=0
        for j in range(len(ls)):
            if ls[j]==y:
                ls[i],ls[j]=ls[j],ls[i]
                i+=1
            print(ls)
        return "".join(ls)
