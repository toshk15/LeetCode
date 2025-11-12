def checkPerfectNumber(num):
    if num==1:
        return False

    sumTarget=1
    n=2

    while n*n<=num:
        if num%n==0:
            sumTarget+=n               
            if n!=num//n:
                sumTarget+=num//n
        n+=1
    if sumTarget==num:
        return True
    else:
        return False
     

"""
Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:

Input: num = 7
Output: false

"""