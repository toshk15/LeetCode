from collections import defaultdict

def findTarget(nums, target):
    dp = defaultdict(int)
    dp[0] = 1

    for i in range(len(nums)):
        next_dp = defaultdict(int)
        for curr_sum, count in dp.items():
            next_dp[curr_sum + nums[i]] += count
            next_dp[curr_sum - nums[i]] += count
        dp = next_dp
    return dp[target]

nums=[1,1,1,1,1]
print(findTarget(nums, 3))

"""
Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1

"""