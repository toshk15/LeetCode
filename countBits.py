def hammingWeight(n):
    b=bin(n)
    b=b[2:]
    m=b.count('1')
    return m
