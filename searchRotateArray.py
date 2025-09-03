"""
def searchArray(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        
        #left sorted portion
        if arr[l] <= arr[mid]:
            if target > arr[mid] or target < arr[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        else:
            if target < arr[mid] or target > arr[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1
"""
def searchArray(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r)//2
        if arr[mid] == target:
            return mid
        
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


arr = [8,9,1,2,4]
print(searchArray(arr, 9))


