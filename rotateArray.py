
def rotate(arr, k):

    l, r = 0 , len(arr) - 1
    k = k % len(arr)

    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1

    l, r = 0, k-1

    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1
    
    l, r = k, len(arr)-1

    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1
    

    return arr
"""
def rotate(nums, k):
    k %= len(nums)
    print(nums[-k:])
    print(nums[:-k])
    nums[:] = nums[-k:] + nums[:-k]
    return nums
"""
arr = [1,4,5,6,7,8,9,10]
print(rotate(arr, 3))

