
import math

#for i in range(4,0,-1):
#    print(i)


#print(math.ceil(3/2))
#print(math.floor(3/2))

#arr = [1] * 5
#print(arr)
"""
arr=[1,2,3]
print(arr[-1])
print(arr[-2])

nums = [1,2,3,4]
print(nums[1:3])
print(nums[0:4])

for i, j in enumerate(nums):
    print(i,j)

n1 = [1,3,5]
n2 = [3,5,6]

for i, j in zip(n1,n2):
    print(i,j)

"""
"""
arr = [5,2,7,3,8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr=["bob", "alice", "jon", "tim"]
arr.sort()

arr.sort(key=lambda x: len(x))
print(arr)

#list comprehension

arr = [[0]*4 for i in range(4)]
print(arr)

"""

x=[chr(i) for i in range(ord("a"),ord("z")+1)]
print(x)
x="".join(x)
print(x)

