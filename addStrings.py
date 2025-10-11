def addStrings(num1,num2):
    n=len(num1)-1
    m=len(num2)-1
    res=[]
    c=0
    while n>=0 or m>=0 or c>0:
        n1 = int(num1[n]) if n >= 0 else 0
        n2 = int(num2[m]) if m >= 0 else 0         
                
        s=n1+n2+c
        st=s%10
        c=s//10           
        res.append(str(st))
        n-=1
        m-=1
    return "".join(res[::-1])