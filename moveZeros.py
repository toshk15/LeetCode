def moveZeros(arr):
    i = j = 0

    while j < len(arr):
        if arr[j] == 0:
            j += 1
        else:
            arr[i] = arr[j]
            i+=1
            j+=1
    while i < len(arr):
        arr[i] = 0
        i+=1

    return arr
"""
def moveZeroes(self, nums: List[int]) -> None:
      
        l,r=0,1

        while r<len(nums):
            if nums[l]==0 and nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                r+=1
                l+=1
            elif nums[l]==0 and nums[r]==0:
                r+=1
            elif nums[l]!=0 and nums[r]!=0:                
                r+=1
                l+=1
            elif nums[l]!=0 and nums[r]==0:                
                r+=1
                l+=1
        return nums
"""
arr = [0,0,0,1,2,3]
print(moveZeros(arr))