from collections import Counter

def majorityElement(nums):
    c = Counter(nums)
    res = []
    for key, value in c.items():
        if value/len(nums)> 1/3:
            res.append(key)
    return res



"""
Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]
"""