"""
def notEqualAve(arr):
    arr.sort()
    res=[]

    l, r = 0, len(arr)-1
    while len(res) != len(arr):
        res.append(arr[l])
        l+=1

        if l<=r:
            res.append(arr[r])
            r-=1
    return res
"""
def notEqualAve(arr):
    arr.sort()
    n = len(arr)
    mid = (n+1)//2

    res = []

    for i in range(mid):
        res.append(arr[i])

        if i+mid < n:
            res.append(arr[i+mid])
    return res


arr=[1,2,3,4,5]
print(notEqualAve(arr))


"""

Example 1:

Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]
Explanation:
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.

Example 2:

Input: nums = [6,2,0,9,7]
Output: [9,7,6,2,0]
Explanation:
When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
Note that the original array [6,2,0,9,7] also satisfies the conditions.

"""