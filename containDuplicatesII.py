def containsNearbyDuplicate(nums, k):
    d={}       
    for i,j in enumerate(nums):
        if j in d:
            if abs(d[j]-i)<=k:
                return True
        d[j]=i
    return False

nums = [1,2,3,1]