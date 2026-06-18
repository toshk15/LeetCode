class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s=set(nums)
        ans=[]
        n=list(s)
        res=sorted(n,reverse=True)
        i=0
        while i < len(n) and k>0:
            ans.append(res[i])
            i+=1
            k-=1
        return ans
