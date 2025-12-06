def getSum(a, b):
    x = a ^ b; 
    y = (a & b) << 1
    while y != 0:
        car = (x & y) << 1
        x = x ^ y
        y = car
    return x
 
a = -1
b = 1

print(getSum(a, b))

