class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=0
        for w in sentences:
            w = w.split()
            res=max(len(w),res)
        return res
            
