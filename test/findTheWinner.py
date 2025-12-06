from collections import deque

def findTheWinner(n, k):
    q = deque()

    for i in range(1, n + 1):
        q.append(i)
    while len(q) > 1:
        for i in range(k-1):
            num = q.popleft()
            q.append(num)
        q.popleft()
    return q[0]

n=5
k=2
print(findTheWinner(n, k))

