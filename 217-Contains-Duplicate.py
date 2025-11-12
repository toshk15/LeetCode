from collections import Counter
def containsDuplicate(nums):
    duplicates = set()

    for num in nums:
        if num in duplicates:
            return True
        duplicates.add(num)
    return False

def containsDuplicate(nums):
    c = Counter(nums)
    m = max(c.values())

    if m>1:
        return True
    else:
        return False

nums = [1,2,3,4,1]
print(containsDuplicate(nums))

"""
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


"""