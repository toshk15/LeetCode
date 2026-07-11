class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res=0
        for p in points:
            d=defaultdict(int)
            for q in points:
                dis=(p[0]-q[0])**2 + (p[1]-q[1])**2
                d[dis]+=1
            for k in d:
                res+=(d[k]*(d[k]-1))
        return res
