class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        return [keys for keys,values in c.items() if values==1]
