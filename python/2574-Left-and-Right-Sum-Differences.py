class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        numsleft=[0]*len(nums)
        numsright=[0]*len(nums)
        i=1
        sumdiff=0
        while i<len(nums):
            sumdiff+=nums[i-1]
            numsleft[i]=sumdiff
            i+=1
        j=len(nums)-2
        sumdiff=0
        while j>=0:
            sumdiff+=nums[j+1]
            numsright[j]=sumdiff
            j-=1
        nums=[abs(x-y) for x,y in zip(numsleft,numsright)]
        return nums
        
"""
Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

"""