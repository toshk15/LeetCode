"""
def canIncrease(nums):
    def inInc(nums):
        n=len(nums)
        for idx in range(n-1):
            if nums[idx] >= nums[idx+1]:
                return False
        return True
    
    n=len(nums)
    for i in range(1,n+1):
        if inInc(nums[:i-1]+nums[i:]):
            return True
    return False
"""
"""
def canBeIncreasing(nums):
    n = len(nums)
    res=[]
    c=0
    for j in range(n-1):
        if nums[j]>=nums[j+1]:
            c+=1
               
    if c>1:
        return False
    else:
        return True
"""         
def canIncrease(nums):
    def is_strictly_increasing_without_index(skip_index):
        previous_value = float("-inf")
        for current_index, current_value in enumerate(nums):
            if current_index == skip_index:
                continue


            if previous_value >= current_value:
                return False                 

            previous_value = current_value            

        return True

      
    violation_index = 0

    while violation_index + 1 < len(nums) and nums[violation_index] < nums[violation_index + 1]:
        violation_index += 1


    return is_strictly_increasing_without_index(violation_index) or is_strictly_increasing_without_index(violation_index + 1)
    
#nums=[105,924,32,968]
  
#nums=[1,1,1,1,1]
#nums = [1,2,10,5,7]
#nums = [2,3,1,2]
nums = [3,2,1,2]
print(canIncrease(nums))