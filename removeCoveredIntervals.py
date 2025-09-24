
def removeCoveredIntervals(intervals):
    intervals.sort(key=lambda range:(range[0], -range[1]))
    print(intervals)
    last_interval = intervals[0]
    remove = 0

    for range in intervals[1:]:
        if range[1] <= last_interval[1]:
            remove+=1
        else:
            if range[1]>last_interval[1]:
                last_interval = range
    return len(intervals)-remove

intervals = [[1,4], [3,6], [2,8], [1,2]]
print(removeCoveredIntervals(intervals))
    
"""

students = [
    {'name': 'Alice', 'age': 20, 'score': 85},
    {'name': 'Bob', 'age': 22, 'score': 92},
    {'name': 'Charlie', 'age': 19, 'score': 78}
]

# Sort by 'score'
sorted_by_score = sorted(students, key=lambda student: student['score'])
print(sorted_by_score)

# Sort by 'age' in reverse order
sorted_by_age_desc = sorted(students, key=lambda student: student['age'], reverse=True)
print(sorted_by_age_desc)

data = [['apple', 3], ['banana', 1], ['cherry', 2]]
# Sort by the second element of each tuple (the number)
data.sort(key=lambda item: (item[1], -item[1]))
print(data)
"""

d = {'ale': 2, 'toño': 3, 'tom': 1, 'ben': 9}

d_sorted = sorted(d, key= lambda sor: sor[1], reverse= True)
print(d_sorted)