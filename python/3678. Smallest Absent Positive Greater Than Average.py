class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n=len(nums)
        avg=sum(nums)//n
        avg=max(avg+1,1)
        s=set(nums)
        while avg in s:
                avg+=1
        
        return avg
