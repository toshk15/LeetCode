def countSymmetricIntegers(low, high):
     for num in range(low, high+1):
        res=[]
        sum1=0
        sum2=0
        for i in range(low, high+1):
            s=str(i)
            n=len(s)//2
            if len(s)%2:
                continue
            s1=s[:n]
            s2=s[n:]
            for x in s1:
                sum1+=int(x)
            for x in s2:
                sum2+=int(x)
            if sum1==sum2:
                res.append(i)
                
            sum1=0
            sum2=0
                
        return len(res)
     
"""

def countSymmetricIntegers(low, high):

    def isSymetric(n):
        s=str(n)
        if len(s)%2!=0:
            return False
        
        mid = len(s)//2
        sum_left = 0
        for i in range(mid):
            sum_left+=int(s[i])

        sum_right=0
        for i in range(mid,len(s)):
            sum_right+=int(s[i])
        
        return sum_left==sum_right
    
    count=0
    for n in range(low, high+1):
        if isSymetric(n):
            count+=1
    return count

"""

     
"""
Example 1:

Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:

Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.

"""