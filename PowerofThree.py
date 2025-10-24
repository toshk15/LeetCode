def isPowerOfThree(n):
    for i in range(n):
        if 3**i==n:
            return True
        if 3**i>n:
            return False    
    return False