class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        i=0
        j=0
        while i<len(s) and j<len(spaces):
            if i==spaces[j]:
                res.append(" ")
                j+=1
            else:
                res.append(s[i])
                i+=1
        if i<len(s):
            res.append(s[i:])
        return "".join(res)
        
