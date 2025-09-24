"""
def findMaxLength(nums):
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
"""

def findMaxLength(nums):
    
    sum_to_index = {0: -1}
    max_length = 0
    cumulative_sum = 0
    
    for index, value in enumerate(nums):
        cumulative_sum += 1 if value == 1 else -1
        if cumulative_sum in sum_to_index:
            current_length = index - sum_to_index[cumulative_sum]
            max_length = max(max_length, current_length)
        else:
            sum_to_index[cumulative_sum] = index

    return max_length   

nums = [0,0,1,1,1]
print(findMaxLength(nums))



