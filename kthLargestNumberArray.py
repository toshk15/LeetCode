def findKthLargest(nums, k):
    nums.sort()
    n = nums[-k]
    return n

nums = [3,2,1,5,6,4]
print(findKthLargest(nums, 2))
        