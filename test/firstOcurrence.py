def firstOcurrence(arr, target):
    l, r = 0, len(arr)-1
    first = -1

    while l <= r:
        mid = (l + r)//2
        if arr[mid] == target:
            first = mid
            r = mid-1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return first

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 10
print(firstOcurrence(arr, target))