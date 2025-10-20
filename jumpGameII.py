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