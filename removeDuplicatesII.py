def containsDuplicate(nums, k):

    window = {}

    for index, value in enumerate(nums):
        if value in window and index - window[value] <= k:
            return True
        
        window[value] = index

    return False


nums = [1, 0, 1, 3]
k = 2
print(containsDuplicate(nums, k))