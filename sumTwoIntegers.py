def getSum(a, b):
    while(b != 0):
        tmp = (a&b) << 1
        a = a ^ b
        b = tmp
    return a

a = 3
b = 11

print(getSum(a, b))

