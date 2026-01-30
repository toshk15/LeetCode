class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res=[]
        setarr=list(set(arr))
        setarr.sort()
        resdict={}
        for i in range(len(setarr)):
            resdict[setarr[i]]=i+1

        for i in arr:
            res.append(resdict[i])
        return res
