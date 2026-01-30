class Solution:
    def capitalizeTitle(self, s: str) -> str:
        res=[]
        ss=s.split(" ")
        for i in ss:
            if len(i)>2:
                res.append(i.capitalize())
            else:
                res.append(i.lower())
        return " ".join(res)
