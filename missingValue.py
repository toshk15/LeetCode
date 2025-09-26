 
def missingValue(nums):
    n = len(nums)     
    sum1 = n * (n+1)//2
    sum2 = sum(nums)
    res = sum1 -sum2
    return res

nums=[0,1]
print(missingValue(nums))