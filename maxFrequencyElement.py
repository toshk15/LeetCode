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

