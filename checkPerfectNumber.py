def checkPerfectNumber(num):
    if num==1:
        return False

    sumTarget=1
    n=2

    while n*n<=num:
        if num%n==0:
            sumTarget+=n               
            if n!=num//n:
                sumTarget+=num//n
        n+=1
    if sumTarget==num:
        return True
    else:
        return False
     