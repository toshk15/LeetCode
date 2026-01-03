class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        s=0
        for i in range(len(nums)):
            if i-k<0 and i+k<=len(nums)-1:
                if nums[i]>nums[i+k]:
                    print(nums[i])
                    s+=nums[i]
            elif i-k >=0 and i+k>len(nums)-1:
                if nums[i]>nums[i-k]:
                    print(nums[i])
                    s+=nums[i]
            elif i-k>=0 and i+k<=len(nums)-1:
                if nums[i-k]<nums[i]>nums[i+k]:
                    print(nums[i])
                    s+=nums[i]
                
        return s

            
            
