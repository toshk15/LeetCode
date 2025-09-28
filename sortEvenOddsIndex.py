def sortEvenOdd(nums):
    even=[]
    odds=[]
    res=[]

    for i in range(len(nums)):
        if i%2==0:
            even.append(nums[i])
        else:
            odds.append(nums[i])
    even.sort()
    odds.sort(reverse=True)
              
    i,j=0,0
    while i<len(even) and j<len(odds):
        res.append(even[i])
        res.append(odds[j])
        i+=1
        j+=1
    while i < len(even):
        res.append(even[i])
        i+=1
    while j < len(odds):
        res.append(odds[j])
        j+=1
    return res