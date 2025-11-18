def trap(height):
    l=0
    r=len(height)-1
    left=height[l]
    right=height[r]
    res=0
    while l<r:
        if left<right:
            l+=1
            left=max(left,height[l])
            res+=left-height[l]
        else:
            r-=1
            right=max(right,height[r])
            res+=right-height[r]
    return res
        

"""
def trap(height):
       
    n = len(height)
    l_max = [0] * n
    r_max = [0] * n

    l_max[0] = height[0]
    r_max[-1] = height[-1]

    result = 0
    for l in range(1, n):
        l_max[l] = max(l_max[l-1], height[l])

    for r in range(n-2, -1, -1):
        r_max[r] = max(r_max[r+1], height[r])

    for i in range(1, n-1):
        result += min(l_max[i], r_max[i]) - height[i]
       
    return result
"""
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))