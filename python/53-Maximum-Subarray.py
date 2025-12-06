def maxSubArray(nums):
    """
    max_sum = nums[0]
    curr_max = nums[0]

    for i in range(1, len(nums)):
        curr_max = max(nums[i], nums[i]+curr_max)
        max_sum = max(curr_max, max_sum)
    return max_sum
    """
    max_sum=nums[0]
    prev_sum=nums[0]

    for i in range(1,len(nums)):
        if prev_sum<0:
            prev_sum = nums[i]
        else:
            prev_sum = prev_sum+nums[i]
        if prev_sum>max_sum:
            max_sum = prev_sum
    return max_sum

arr = [3,-7,10, 2,-2]

print(maxSubArray(arr))