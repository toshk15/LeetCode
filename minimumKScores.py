def minimumDifference(nums, k):
    nums.sort()
    l, r = 0, k-1
    res = float("inf")

    while r < len(nums):
        res = min(res, nums[r]-nums[l])
        l, r = l+1, r+1
    return res
nums=[3,1,9,0,3,7]
print(minimumDifference(nums,3))
