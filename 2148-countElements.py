def countElements(self, nums):
    M = max(nums)
    m = min(nums)
    return sum(1 for i in nums if m<i<M)

"""
def countElements(self, nums):
    c={}
    for i in nums:
        c[i] = 1 + c.get(i,0)

    minimum = min(nums)
    maximum = max(nums)
 
    if minimum==maximum:
        return len(nums)-c[maximum]
    else:
        return len(nums)-c[maximum]-c[minimum]
"""