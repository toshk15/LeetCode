class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        start, end = intervals[0]
        res=[]
        for s,e in intervals[1:]:
            if end>=s:
                start=min(start,s)
                end=max(end, e)
            else:
                res.append([start, end]) 
                start,end=s,e  
        res.append([start,end])        
        return res
    
"""
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""