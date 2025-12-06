def minSubArrayLen(target, nums):
    sumT=nums[0]  
    l=0
    r=0   
    res=float('inf')
    n=len(nums)
    while r<n:       
        if sumT>=target:
            res= min(res,(r-l+1))
            sumT= sumT-nums[l]
            l+=1
        else:
            r+=1
            if r<n:
                sumT+=nums[r]
    return res if res<float('inf') else 0


"""
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r-l+1)

                total -= nums[l]
                l+=1
        if res == float('inf'):
            return 0
        else:
            return res

"""

nums=[2,3,1,2,4,3] 
#nums=[1,4,4]
#nums = [1,1,1,1,1,1,1,1]
print(minSubArrayLen(7,nums))