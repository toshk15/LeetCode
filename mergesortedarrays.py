"""
def merge(L1, m, L2, n):
    max_size = m + n -1

    while n >= 0 and m>=0:

        if L1[m-1] < L2[n-1]:
            L1[max_size] = L1[m-1]
            m -= 1            
        else:
            L1[max_size] = L2[n-1]
            n -= 1
        max_size -= 1

    return L1
"""

def merge(L1, m, L2, n):
    res = [None] * (m + n)
    while m > 0 and n > 0:
        if L1[m-1] >= L2[n-1]:
            res[m+n-1] = L1[m-1]
            m -= 1
        else:
            res[m+n-1] = L2[n-1]
            n -= 1
    #print(res)
    if n > 0:
        res[:m+n] = L2[:n] 
    if m > 0:
        res[:m+n] = L1[:m]  
    return res   

    


L1 = [1,2,4,7,8]
L2 = [3,5,6]

print(merge(L1, 5, L2, 3))


