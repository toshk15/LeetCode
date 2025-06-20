def searchArray(arr, target):
    l, r = 0, len(arr) - 1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return True
        
        #left sorted portion
        if arr[l] < arr[mid]:
            if arr[l] <= target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        elif arr[l] > arr[mid]:
            if arr[mid] < target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            l += 1
    return False

arr = [-2,-2,-2, -1, 1, 2, 8, 10]
print(searchArray(arr, -5))


