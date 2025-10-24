def arraySign(nums):     
    c=0
    for i in nums:
        if i==0:
            return 0
        if i<0:
            c+=1
    if c%2==0:
        return 1
    else:
        return -1
    
nums = [-1,-2,-3,-4,3,2,1]