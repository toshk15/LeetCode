def findKthLargest(nums, k):
    nums.sort()
    n = nums[-k]
    return n

"""
def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
"""

nums = [3,2,1,5,6,4]
print(findKthLargest(nums, 2))
        