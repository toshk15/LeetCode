def contigous_array(nums):
    zero, one = 0, 0
    res = 0
    diff = {}

    for i, n in enumerate(nums):
        if n==0:
            zero+=1
        else:
            one+=1
        if one - zero not in diff:
            diff[one-zero] = i
        
        if one == zero:
            res = one+zero
        else:
            idx = diff[one-zero]
            res = max(res, i-idx)
    return res

nums = [0,0,1,1,1]
print(contigous_array(nums))



