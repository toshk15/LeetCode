class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        print(intervals)
        first, second = intervals[0]
        remove = 0
        for f,s in intervals[1:]:
            if s<=second:
                remove+=1                       
            else:
                first,second = f,s
        return len(intervals)-remove

"""
Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1

"""

