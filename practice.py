"""
def sumTwo(arr, target):
    
    nums={}   

    for x, y in enumerate(arr):

        diff = target - y
        
        if diff in nums:
            return [nums[diff], x]
        nums[y] = x

arr = [0, 2, 3, 4, 8]
print(sumTwo(arr, 7))

"""
def repeating(s):

    c = {}

    for i in s:
        c[i] = 1 + c.get(i,0)

    for i , j in c.items():
        if j == 1:
            return i
        else: 
            continue
    return ""

    

s = "aabcc"
print(repeating(s))
 