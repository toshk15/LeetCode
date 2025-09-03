"""
def product(nums):
    res = [1] * len(nums)

    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    posfix = 1

    for i in range(len(nums)-1, -1, -1):
        res[i] *= posfix
        posfix *= nums[i]
    return res
"""

def product(nums):    

        num_length = len(nums)  
        answer = [1] * num_length
        left = 1

        for i in range(num_length):
            answer[i] = left
            left *= nums[i]

        right = 1

        for i in range(num_length - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer
"""
def product(nums):
    arr=[]
    for j in range(len(nums)):
        pro = 1
        for i in range(len(nums)):
            if i == j:
                continue
            else:
                pro = pro * nums[i]
        arr.append(pro)   
    return arr
"""

nums = [1,2,3,4]

print(product(nums))
