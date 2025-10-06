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

