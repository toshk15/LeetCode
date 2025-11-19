class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1,p2,p3=points

        if p1==p2 or p1==p3 or p2==p3:
            return False
        #m1 = p2[1]-p1[1]//p2[0]-p1[0]
        #m2 = p3[1]-p2[1]//p3[0]-p2[0]
        #m3 = p3[1]-p1[1]//p3[0]-p1[0]
        return (p2[1]-p1[1]) * (p3[0]-p1[0]) != (p2[0]-p1[0]) * (p3[1]-p1[1])
    

"""
Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false

"""