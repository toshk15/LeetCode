def arraySign(nums):
    flag = True
    for x in nums:
        if x == 0:
            return 0
        
        if x < 0:
            flag = not flag
    return 1 if flag else -1

nums = [1,-2,-3,-4, 2, 9]
print(arraySign(nums))

"""
Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

"""