def canJump(nums):
    n = len(nums)
    nf=n-1
        
    for i in range(n-2,-1,-1):
        if i+nums[i]>=nf:
            nf = i
    if nf==0:
        return True
    else:
        return False
    
nums = [2,3,1,1,4]  

"""
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

"""