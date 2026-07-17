class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = abs(sum(nums)-goal)
        min_ele=(s+limit-1)//limit
        return min_ele
