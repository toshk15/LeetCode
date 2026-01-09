class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indices = [i for i, x in enumerate(nums) if x == 1]
        for n in range(len(indices)-1):
            if (indices[n+1]-indices[n])-1<k:
                return False
        return True
            
