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