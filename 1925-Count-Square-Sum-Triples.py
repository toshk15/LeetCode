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


"""
Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

"""