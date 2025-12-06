def sortEvenOdd(nums):
    even=[]
    odds=[]
    res=[]

    for i in range(len(nums)):
        if i%2==0:
            even.append(nums[i])
        else:
            odds.append(nums[i])
    even.sort()
    odds.sort(reverse=True)
              
    i,j=0,0
    while i<len(even) and j<len(odds):
        res.append(even[i])
        res.append(odds[j])
        i+=1
        j+=1
    while i < len(even):
        res.append(even[i])
        i+=1
    while j < len(odds):
        res.append(odds[j])
        j+=1
    return res

"""
 

Example 1:

Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation: 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].

Example 2:

Input: nums = [2,1]
Output: [2,1]
Explanation: 
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array. 

"""