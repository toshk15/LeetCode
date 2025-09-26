def removeDuplicates(nums):
    k = 1
    l = 1
    j = 1
    n = len(nums)

    while j < n:
        if nums[l-1] == nums[j]:                
               j+=1
        else:
            nums[l] = nums[j]
            k+=1
            l+=1
    return k

nums=[1,1,2]
print(removeDuplicates(nums))