class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d={v[0]:k for k,v in enumerate(pieces)}
        res=[]
        for i in arr:
           if i in d:
              res.extend(pieces[d[i]])
        return res==arr
