"""
def twoSum(arr, target):
   
    l, r = 0, len(arr) - 1
    arr = sorted(arr)
    res = []
    while l < r:
        s = arr[l] + arr[r]

        if target > s:
            l += 1
        elif target < s:
            r -= 1
        else:
            res.append([arr[l] , arr[r] ])
            l += 1
            r -= 1
    return res
"""


def twoSum(arr, target):

    count = {}

    for i, num in enumerate(arr):
        res = target - num

        if res in count:
            return [count[res] , i]

        count[num] = i
            


arr = [0, 2, 3, 4, 8]
k = 7
print(twoSum(arr, k))

