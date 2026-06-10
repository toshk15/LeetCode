class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        t=text.split(" ")
        res=[]
        for i in range(len(t)-2):
            if t[i]==first and t[i+1]==second:
                res.append(t[i+2])
        return res
            
