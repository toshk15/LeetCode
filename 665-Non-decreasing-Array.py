"""
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
"""
"""
def noDecreasing(nums):
    if len(nums)<=2:
        return True
    c=0
    for n in range(len(nums)):
        if n==len(nums)-1 or nums[n]<=nums[n+1]:
            continue
        if n==0 or nums[n+1]>=nums[n-1]:
            nums[n]=nums[n+1]
            c+=1
        else:
            nums[n+1]=nums[n]
            c+=1
    if c>1:
        return False
    else:
        return True
 """   

def noDecreasing(nums):
    changed = 0

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if changed == 1:
                return False
            changed += 1

            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]

    return True

 
nums = [1,2,2,1,1]
#nums = [1,2,3,4,5,1,1]
#nums = [4,2,1]
#nums = [4,2,3]

print(noDecreasing(nums))

"""
Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You cannot get a non-decreasing array by modifying at most one element.

"""