def isMonotonic(nums):
    f = [1 if nums[0]<nums[-1] else 0]
    if f[0]:
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]<=nums[j]:
                continue
            else:
                return False
    else:
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]>=nums[j]:
                continue
            else:
                return False
    return True

nums = [6,5,4,4]