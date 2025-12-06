"""
def mergeIntervals(intervals):
    intervals.sort(key = lambda x : x[0])
    output = [intervals[0]]

    for start, end in intervals:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd,end)
        else:
            output.append([start, end])
    return output
"""

def mergeIntervals(intervals):
 
    intervals.sort()
    merged_intervals = []

    curr_start, curr_end = intervals[0]

    for start, end in intervals[1:]:
        if curr_end < start:
            merged_intervals.append([curr_start, curr_end])
            curr_start, curr_end = start, end
        else:
            curr_end = max(curr_end, end)

    merged_intervals.append([curr_start, curr_end])     

    return merged_intervals

#inter =[[1,4],[4,5]]
inter = [[1,3], [2,6], [8,10], [15,18]]
print(mergeIntervals(inter))


"""
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

"""
