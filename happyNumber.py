def isHappy(n):
    d={}
    s=0
    while True:
        while n!=0:
            s += (n % 10) ** 2
            n = n // 10             

        if s == 1:
            return True
                
        n = s
        s=0

        if n in d:
            return False
        d[n]=1
n=19
print(isHappy(n))