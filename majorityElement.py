"""


def majorityElement(nums):
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res

nums = [1,2,3,2,1,2,1,2]
print(majorityElement(nums))



def majorityElement(nums):
    count = 0
    max_majority= None

    for num in nums:

        if count == 0:
            max_majority = num
            count = 1
        elif max_majority == num:
            count += 1
        else:
            count -= 1
    return max_majority

def majorityElement(self, nums: List[int]) -> int:
    res, count = 0,0
    for n in nums:
        if count == 0:
            res = n
        count +=(1 if n== res else -1)
    return res 
"""

def majorityElement(nums):
    count = {}
    res, maxCount = 0, 0

    for n in nums:
        count[n] = 1 + count.get(n,0)
        res = n if count[n] > maxCount else res
        maxCount = max(count[n], maxCount)
    return res

nums = [1,1,2,2,2,3,3]
print(majorityElement(nums))