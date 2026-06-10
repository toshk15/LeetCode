class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d={n:idx for idx,n in enumerate(nums)}
        for pos,curr in operations:
            i = d[pos]
            nums[i]=curr
            del d[pos]
            d[curr]=i
        return nums
