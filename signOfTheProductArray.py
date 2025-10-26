def arraySign(nums):
    flag = True
    for x in nums:
        if x == 0:
            return 0
        
        if x < 0:
            flag = not flag
    return 1 if flag else -1

nums = [1,-2,-3,-4, 2, 9]
print(arraySign(nums))