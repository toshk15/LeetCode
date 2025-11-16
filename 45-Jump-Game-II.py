def jump(nums):
    l,r=0,0
    f=0
    n=len(nums)
    res=0
    
    while r<n-1:
        for i in range(l,r+1):
            f=max(f,i+nums[i])

        l=r+1
        r=f
        res+=1
    return res

nums = [2,3,1,1,4]
print(jump(nums))


"""
Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

"""