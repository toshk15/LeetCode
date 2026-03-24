class Solution:
    import random

    def __init__(self, nums: List[int]):
        self.res=nums

    def reset(self) -> List[int]:
        return self.res
        
    def shuffle(self) -> List[int]:
        self.aux=self.res[:]
        random.shuffle(self.aux)
        return self.aux
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
