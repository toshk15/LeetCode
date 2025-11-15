from collections import Counter

def maxFrequencyElements(nums):
    d = Counter(nums)
    d_values = max(d.values())
    res=0

    for key, values in d.items():
        if values == d_values:
            res+=values
    return res

nums = [1,2,2,3,1,4]
print(maxFrequencyElements(nums))

"""
Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

"""