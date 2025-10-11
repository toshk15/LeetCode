def reverseBits(n):
    b = bin(n)[2:]
    x = len(b)
    m = 32-x
    b='0'*m+b
    sr=b[::-1]
    d=int(sr,2)
    return d

def reverseBits(n):
    result = 0
    for _ in range(32):
        bit = n & 1
        result = (result << 1) | bit
        n >>= 1
    return result