from collections import deque
"""
def sliding_window_maximum(arr, k):
    output = []
    q = deque()
    l = r = 0

    while r < len(arr):
        while q and arr[q[-1]] < arr[r]:
            q.pop()
        q.append(r)
        #print(q[0])
        if l > q[0]:
            q.popleft()
        
        if (r+1) >= k:
            output.append(arr[q[0]])
            l+=1
        r+=1
    return output

"""
def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

    q = deque()
    res = []

    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(i)

        if q[0] == i - k:
            q.popleft()
        if i >= k - 1:
            res.append(nums[q[0]])

    return res


arr = [3,3,1,1,1]
k = 3
print(sliding_window_maximum(arr, k))



    