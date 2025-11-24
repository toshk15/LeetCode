class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        res=[]

        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            elif nums[i]%2==1:
                odd.append(nums[i])
        i=0    
        while i < len(even) or i<len(odd):
            res.append(even[i])  
            res.append(odd[i]) 
            i+=1
     
        return res
    
"""
Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:

Input: nums = [2,3]
Output: [2,3]

"""