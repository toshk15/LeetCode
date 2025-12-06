def isArraySpecial(arr):
    for i in range(1, len(arr)):
        if arr[i] % 2 == arr[i-1] % 2:
            return False
    return True

#arr = [1,2,3]
arr = [1,2,3,5]
print(isArraySpecial(arr))

"""

Example 1:

Input: nums = [1]

Output: true

Explanation:

There is only one element. So the answer is true.

Example 2:

Input: nums = [2,1,4]

Output: true

Explanation:

There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

Input: nums = [4,3,1,6]

Output: false

Explanation:

nums[1] and nums[2] are both odd. So the answer is false.

"""