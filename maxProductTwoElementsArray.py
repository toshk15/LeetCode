import heapq

def maxProduct(self, nums):
    for i in range(len(nums)):
        nums[i] = -nums[i]
    heapq.heapify(nums)

    n1 = -heapq.heappop(nums)
    n2 = -heapq.heappop(nums)

    return (n1-1) * (n2-1)

    #better solution
    """
    nums.sort(reverse=True)
        n1=nums[0]-1
        n2=nums[1]-1
        return n1*n2
    """

nums=[3,4,5,2]
print(maxProduct(nums))