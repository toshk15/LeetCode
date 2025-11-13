def eraseOverlapINtervals(intervals):
    intervals.sort()

    res = 0
    firstEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= firstEnd:
            firstEnd = end
        else:
            res+=1
            firstEnd = min(end, firstEnd)
    return res

intervals = [[1,2], [2,3], [3,4],[1,3]]
print(eraseOverlapINtervals(intervals))

"""
Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

"""