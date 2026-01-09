class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            sk=0
            for ele in piles:
                sk+=math.ceil(float(ele)/k)
            if sk<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res
