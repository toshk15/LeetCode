def countSymmetricIntegers(low, high):
     for num in range(low, high+1):
        res=[]
        sum1=0
        sum2=0
        for i in range(low, high+1):
            s=str(i)
            n=len(s)//2
            if len(s)%2:
                continue
            s1=s[:n]
            s2=s[n:]
            for x in s1:
                sum1+=int(x)
            for x in s2:
                sum2+=int(x)
            if sum1==sum2:
                res.append(i)
                
            sum1=0
            sum2=0
                
        return len(res)
