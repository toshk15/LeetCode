def isPowerOfFour(n):
    if n<=0:
        return False

    for i in range(0,n):
        if 4**i==n:
            return True
        if 4**i>n:
            return False