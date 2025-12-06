
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

"""
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""