class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = Counter(nums)
        freq = max(c.values())
        index1=defaultdict(int)
        index2=defaultdict(int)
        maxFreq=float("inf")
        for i,j in enumerate(nums):
            if j not in index1:
                index1[j]=i
            index2[j]=i

        for n in nums:
            if c[n]==freq:
                diff = index2[n]-index1[n] + 1
                maxFreq=min(maxFreq,diff)
        return maxFreq
                
"""
Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

"""