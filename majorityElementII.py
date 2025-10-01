from collections import Counter

def majorityElement(nums):
    c = Counter(nums)
    res = []
    for key, value in c.items():
        if value/len(nums)> 1/3:
            res.append(key)
    return res