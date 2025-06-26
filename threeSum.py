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


nums = [2, -2, -2, 2, 4, 0, 10]
print(threeSum(nums))

