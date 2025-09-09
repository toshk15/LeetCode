def maxArea(container):
    #brute force approach
    """
    res = 0

    for l in range(len(container)):
        for r in range(l+1, len(container)):
            area = (r-l) * min(container[l], container[r])
            res = max(res, area)
    return res
    """
    res=0
    l,r = 0, len(container)-1
    while l < r:
        area = (r-l) * min(container[l], container[r])
        res = max(res, area)

        if container[l] < container[r]:
            l+=1
        else:
            r-=1
    return res

container=[1,4,2,6,0,5,5,9,4]
print(maxArea(container))


