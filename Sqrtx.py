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
        