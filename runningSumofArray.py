def runningSum(nums):
    n=len(nums)
    new = [0]*n
    s=0

    for i in range(n):
        s+=nums[i]
        new[i]=s
    return new
        
nums = [1,2,3,4]