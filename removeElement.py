"""
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        i+=1
    return nums
"""
def removeElement(nums, val):
    n = len(nums)
    i = 0

    while i < n:
        if nums[i] == val:
            nums[i], nums[n-1] = nums[n-1], nums[i]
            n -= 1
        else:
            i += 1
    return n
      
nums = [1,3,4,4,5,6]
print(removeElement(nums, 4))
