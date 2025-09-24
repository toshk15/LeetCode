from collections import Counter
def twoSum(numbers, target):
    l, r = 0, len(numbers)-1
    while l <= r:
        res = numbers[l] + numbers[r]
        if target < res:
            r = r-1
        elif target > res:
            l = l+1
        else:
            return [l+1, r+1]
        

print(twoSum)