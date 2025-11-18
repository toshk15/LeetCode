"""
def threeSum(nums):

    res = []
    nums.sort()

    for i, j in enumerate(nums):
        print(i, j)

        if j > 0:
            break

        if i > 0 and j == nums[i -1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            threeSum = j + nums[l] + nums[r]

            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([j, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == [l - 1] and l < r:
                    l += 1
    return res



def sum_three_numbers(nums):
    res= []
    nums.sort()
    for i in range(len(nums)-1):

        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:

            sumT = nums[i] + nums[l] + nums[r]

            if sumT > 0:
                r -= 1
            elif sumT < 0:
                l += 1
            else:
                res.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l<r:
                    l += 1
        return res
"""
def sum_three_numbers(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i-1]:
            continue

        results = result_sum(nums, i + 1, -nums[i])

        for x in results:
            res.append([nums[i]] + x)
    return res

def result_sum(nums, start,target):
    p = []
    l, r = start, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            p.append([nums[l], nums[r]])
            l += 1

            while l < r and nums[l] == nums[l-1]:
                l+=1
        elif s < target:
            l+=1
        else:
            r-=1
    return p



nums = [2, -2, -2, 2, 4, 0, 10]
print(sum_three_numbers(nums))

