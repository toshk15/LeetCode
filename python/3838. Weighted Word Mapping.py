class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=[]
        for w in words:
            s=0
            for ww in w:
                s+=weights[ord(ww)-ord("a")]
            res.append(chr(ord("z")-(s%26)))
        return "".join(res)
            
