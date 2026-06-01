class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = defaultdict(int)
        kk=None
        valmax=float("-inf")
        for i in range(len(nums)-1):
            if key == nums[i]:
                d[nums[i+1]]+=1
        for k,v in d.items():
            if v>valmax:
                valmax=v
                kk=k
        return kk
