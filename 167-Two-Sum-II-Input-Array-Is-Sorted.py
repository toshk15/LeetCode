from collections import Counter
def twoSum(numbers, target):
    l, r = 0, len(numbers)-1
    while l <= r:
        res = numbers[l] + numbers[r]
        if target < res:
            r = r-1
        elif target > res:
            l = l+1
        else:
            return [l+1, r+1]
        

print(twoSum)

"""
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

"""