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