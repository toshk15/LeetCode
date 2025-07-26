def find_all_per(nums):
    res = []
    backtrack(nums, [], set(), res)
    return res

def backtrack(nums, candidate, used, res):
    if len(candidate) == len(nums):
        res.append(candidate[:])
        return
    for num in nums:
        if num not in used:
            candidate.append(num)
            used.add(num)
            backtrack(nums, candidate, used, res)
            candidate.pop()
            used.remove(num)
nums = [1,2]
print(find_all_per(nums))
