"""
def sortedRotated(arr):
    n = len(arr)
    count = 1

    for i in range(1, 2*n):
        if arr[(i-1)%n] <= arr[i%n]:
            count += 1
        else:
            count = 1
        if count == n:
            return True
    return n == 1
"""
def check(nums):
    c=0
    if nums[-1]>nums[0]:
        c+=1      

    for i in range(1,len(nums)):
        if nums[i-1]<=nums[i]:
            continue
        else:
            c+=1
    return False if c>=2 else True


arr = [3,4,5,1,2]
print(check(arr))