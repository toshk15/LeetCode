def getSum(a, b):
    a=bin(a)
    a=a[2:]
    b=bin(b)
    b=b[2:]
    c = a & b
    return int(c)
 
a = -1
b = 1

print(getSum(a, b))

