def searchPos(arr, target):
    left = search(arr, target, True)
    right = search(arr, target, False)
    return [left, right]

def search(arr,target, flag):
    l, r = 0, len(arr) - 1
    i = -1

    while l <= r:
        m = (l + r) // 2
        if target > arr[m]:
            l = m + 1
        elif target < arr[m]:
            r = m - 1
        else:
            i = m
            if flag:
                r = m - 1
            else:
                l = m + 1
    return i

arr = [-2, -1, 1, 1, 1, 2, 3, 4]
print(searchPos(arr, 1))
