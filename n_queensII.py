def n_queens(k, x, n):

    for i in range(1, n+1):
        if valid(k, i):
            x[k] = i

            if k == n:
                print(x)
                return
            
            n_queens(k+1, x, n)

def valid(k, l):
    for i in range(1, k):
        if x[i] == l or abs(i-k) == abs(x[i]-l):
            return False
    return True

n = 4
x = [0,0,0,0,0]
k=1
n_queens(k,x,n)