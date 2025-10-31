def isArraySpecial(nums):
    for i in range(1,len(nums)):
        if (nums[i-1]%2==0 and nums[i]%2==1) or (nums[i-1]%2==1 and nums[i]%2==0):
            continue
        else:
            return False
    return True


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