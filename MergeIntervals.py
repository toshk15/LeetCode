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
