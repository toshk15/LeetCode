class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res=0
        n=len(colors)
        colors+=colors
        for i in range(n):
            j=i+1
            k=i+2
            if colors[i]!=colors[j] and colors[j]!=colors[k]:
                res+=1
        return res
