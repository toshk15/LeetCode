class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        minArea=float("inf")
        seen=set()
        for x1,y1 in points:
            for (x2,y2) in seen:
                if (x1,y2) in seen and (x2,y1) in seen:
                    d=abs(x2-x1)*abs(y2-y1)
                    minArea=min(minArea,d)
            seen.add((x1,y1))
        return minArea if minArea!=float("inf") else 0
