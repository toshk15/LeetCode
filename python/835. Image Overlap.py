class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        c=Counter()
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img1[i][j]==1:
                    for ii in range(len(img2)):
                        for jj in range(len(img2)):
                            if img2[ii][jj]==1:
                                d=(i-ii,j-jj)
                                c[d]+=1
        return max(c.values()) if c else 0
