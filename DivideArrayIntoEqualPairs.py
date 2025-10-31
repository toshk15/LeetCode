from collections import Counter

def divideArray(nums):
    n=len(nums)
    if n%2==1:
        return False

    c=Counter(nums)
    for i in c.values():
        if i%2!=0:
            return False
    return True

"""

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
"""