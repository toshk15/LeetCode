def sortedSquare(nums):
    l, r = 0, len(nums)-1
    result = [None] *(len(nums))

    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])
        if left > right:
            result[r-l] = left * left
            l+=1
        else:
            result[r-l] = right * right
            r-=1
    return result

nums=[-3, -2, -1, 3, 9]
print(sortedSquare(nums))
