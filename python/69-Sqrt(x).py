def mySqrt(x):
    if x==1:
        return 1
    l=0
    r=x
    res=0

    while l<=r:          
        m=l+((r-l)//2)

        if m**2>x:
            r=m-1                
        elif m**2<x:
            l=m+1  
            res=m            
        else:
            return m
    return res

"""       
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""