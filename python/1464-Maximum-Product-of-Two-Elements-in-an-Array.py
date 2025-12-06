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
"""
nums=[3,4,5,2]
print(maxProduct(nums))


Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:

Input: nums = [3,7]
Output: 12
"""