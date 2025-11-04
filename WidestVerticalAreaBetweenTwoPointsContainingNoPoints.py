class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points=sorted(points, key=lambda point:point[0])
        m=float("-inf")
        for i in range(1,len(points)):
            ma= points[i][0]- points[i-1][0]
            m=max(m,ma)
        return m


​
"""
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.

Example 2:

Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3
"""