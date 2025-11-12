def isHappy(n):
    d={}
    s=0
    while True:
        while n!=0:
            s += (n % 10) ** 2
            n = n // 10             

        if s == 1:
            return True
                
        n = s
        s=0

        if n in d:
            return False
        d[n]=1
n=19
print(isHappy(n))

 
"""
Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false
"""