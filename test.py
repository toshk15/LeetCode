def getmax(interval):

    if len(interval) == 0:
        return 0
    s = min(a)
    x = max(a)
    ss = min(s)
    xx = max(x)
    
    counter = []
    for i in range(ss, xx+1):
        c = 0
        for j in range(len(interval)):        
            if interval[j][0] <= i <=interval[j][1]:          
                c+=1
        counter.append(c)
    co = max(counter)
    return co

                
          

#a = [[1,3], [2,4], [3,6]]
a = [[]]
if a is not None:
    print(len(a[0]))
else:
    print("o")
#print(getmax(a))