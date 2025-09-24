def noDecreasing(nums):
    if len(nums) <= 2:
        return True
    
    change = False
    for i, num in enumerate(nums):
        if i == len(nums) - 1 or num <= nums[i+1]:
            continue
        if change:
            return False
        if i == 0 or nums[i+1] >= nums[i-1]:
            nums[i] = nums[i+1]
        else:
            nums[i+1] = nums[i]
        change = True
    return True

nums = [1,2,5,4]

print(noDecreasing(nums))