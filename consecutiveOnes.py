def findMaxConsecutiveOnes(nums):
    c = 0
    maxi = 0
    for i in nums:
        if i == 1:
            c+=1                           
        else:
            maxi = max(maxi, c)
            c=0

    return max(maxi, c)