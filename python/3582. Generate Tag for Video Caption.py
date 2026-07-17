class Solution:
    def generateTag(self, caption: str) -> str:
        s=caption.split()
        res=[n.capitalize() for n in s]
        if res:
            res[0]=res[0].lower()
        res="#"+"".join(res)
        return res[:100]
