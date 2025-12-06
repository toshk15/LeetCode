"""
def sumTwo(arr, target):
    
    nums={}   

    for x, y in enumerate(arr):

        diff = target - y
        
        if diff in nums:
            return [nums[diff], x]
        nums[y] = x

arr = [0, 2, 3, 4, 8]
print(sumTwo(arr, 7))


def repeating(s):

    c = {}

    for i in s:
        c[i] = 1 + c.get(i,0)

    for i , j in c.items():
        if j == 1:
            return i
        else: 
            continue
    return ""

    

s = "aabcc"
print(repeating(s))


def product(nums):

    ans = [1] * len(nums)
    left = 1

    for i in range(len(nums)):
        ans[i] = left
        left *= nums[i]

    right = 1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans

nums=[1,2,3,4]
print(product(nums))
"""

