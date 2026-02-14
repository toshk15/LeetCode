class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l=len(arr)
        n=l//20
        res=arr[n:l-n]
        return sum(res)/len(res)
