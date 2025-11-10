def binarySearch(arr, target):

    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        
        if target > arr[mid]:
            l = mid + 1
        elif target < arr[mid]:
            r = mid - 1
        else:
            return True
    return False

arr = [1,2,3,4,5,6,7,8]

print(binarySearch(arr, -8))


"""
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

