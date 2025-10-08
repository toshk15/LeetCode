"""
def countTriples(n):
    res=[]
    c = [i*i for i in range(1,n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            r=i**2 + j**2
            if r in c:
                res.append((i,j,r))
    return len(res)


def countTriples(n):
    ans = 0
    squared = set()

    for i in range(1, n + 1):
      squared.add(i * i)

    for a in squared:
      for b in squared:
        if a + b in squared:
          ans += 1

    return ans

"""

def countTriples(n):
    res=0
    c = [i*i for i in range(1,n+1)]
    for i in c:
        for j in c:
            r=i+j
            if r in c:
                res+=1
    return res

n=10
print(countTriples(n))