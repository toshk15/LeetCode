"""
from collections import defaultdict
def counBandPairs(nums):

    good_pairs = 0
    total_pairs = 0
    count = defaultdict(int)
    for i in range(len(nums)):
        total_pairs += i
        good_pairs += count[nums[i] - i]
        count[nums[i] - i] += 1

    return total_pairs - good_pairs

nums = [1,1,3,3] 
#nums = [3,3,1,1] 
print(counBandPairs(nums))   
"""

def countBandPairs(nums):
    good_pairs = 0
    total_pairs = 0
    count = {}

    for i in range(len(nums)):
        total_pairs += i
        count[nums[i] - i] = count[nums[i] - i]  if count.get((nums[i] - i),0) != 0 else 0  
        good_pairs += count[nums[i] - i]     
        count[nums[i] - i] += 1

    return total_pairs - good_pairs

nums = [1,1,3,3] 
print(countBandPairs(nums)) 