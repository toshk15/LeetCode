def binarySearch(arr, target):

    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        
        if target > arr[mid]:
            l = mid + 1
        elif target < arr[mid]:
            r = mid - 1
        else:
            return True
    return False

arr = [1,2,3,4,5,6,7,8]

print(binarySearch(arr, -8))
    
