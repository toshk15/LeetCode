def maxDistance(arrays):
    maximum = arrays[0][-1]
    minimum = arrays[0][0]
    s3=float("-inf")

    for n in range(1,len(arrays)):
        s1=maximum-arrays[n][0]
        s2=arrays[n][-1]-minimum
        maximum=max(maximum,arrays[n][-1])
        minimum=min(minimum,arrays[n][0])
        s3=max(s3,s1,s2)
    return s3


"""
Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Example 2:

Input: arrays = [[1],[1]]
Output: 0
"""