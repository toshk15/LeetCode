"""
def strStr(haystack, needle):
    flag = 1
    s=''
    l,  r = 0,0
    if needle not in haystack:
        return -1
    while l < len(needle) and r < len(haystack):
        if haystack[r] == needle[l]:
            if flag:
                start = r
                flag = 0
            s+=haystack[r]
            l+=1
            r+=1
        elif len(s)>=1:
            s=''
            l=0
            if haystack[r] == haystack[r-1]:
                r = r
            else:
                r-=1
            flag = 1
        else:
            r+=1
            
    print(s)
    if needle in haystack:
        return start        
    else:
        return -1



       
haystack="aabaaabaaac"
needle = "aabaaac"



print(strStr(haystack, needle))


def removeDuplicates(nums):
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[i-1] = nums[i]
            k+=1
        else:
            k+=1
            continue
    return k
nums=[1,1,2]
print(removeDuplicates(nums))


import heapq


numbers = [5, 1, 8, 3, 7]
heapq.heapify(numbers)


k = 8
rsum=0
res=0
y=0
diffleft=0
maximun = 0
nums=[96,90,41,82,39,74,64,50,30]
x = sum(nums[:k])
r = x
#print(x)
for i in range(1,k+1):   
    y = sum(nums[-i:])
    diffleft += nums[k-i]
    rsum = x - diffleft
    res = rsum + y    
    maximun = max(maximun,x, res)
print(maximun)

print(nums[-8:])
print(nums[:8])


str1 = "ertsad"
for i in range(len(str1) - 1, -1, -1):
    print(i)



for i in range(2,-1,-1):
    print(i)
  
def isPalindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    l,r = 0, len(s)-1
    print(s)

    while l<=r:
        if not s[l].isalpha():
            l+=1
        if not s[r].isalpha():
                r-=1           
        if s[l] == s[r]:
            l+=1
            r-=1

        if s[l] != s[r]:
            print(s[l])
            print(s[r])
            return False

    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))


def maxProfit(prices):
    res = 0
        
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)
    return res

nums=[7,1,5,3,6,4]
print(maxProfit(nums))

nums=[1,1,1,2,2,3]
bucket=[0 for i in range(len(nums)+1)]
print(bucket)


from collections import deque

q = deque()
q.append(1)

x=[1,2,3,4]
res=[0]*4
res[0]=x[0]
res[0]=x[1]

print(res)


matrix = [[3,7,8],[9,11,13],[15,16,17]]
m=matrix[0][0]
for i in range(len(matrix)):
    maxi=0
    for j in range(len(matrix)):
        maxi = max(matrix[j][i], m)
    n = min(matrix[i])
    if maxi == n:
        print(n)
 
    

#print(matrix[0])
#print(matrix[1])
#print(matrix[2])

#for i in matrix:
    #print(i[2])
    
#matrix = [[3,7,8],[9,11,13],[15,16,17]]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
t = list(zip(*matrix))
print(t)

for row in range(len(matrix)):
    m = min(matrix[row])
    ma=0
    for col in range(len(t)):
        ma = max(t[col])
        if m == ma:
            print(m,ma)
 

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(mat[0][0])

mat = [[1,1,1],[1,1,0]]
max_ones=0
stack=[]
for idx,row in enumerate(mat):  
    c=row.count(1)
    if c>max_ones:
        stack.append([idx,c])
        max_ones=c
print(stack.pop())

l=1200
h=1230
res=[]
s=''
sum1=0
sum2=0
for i in range(l, h+1):    
    s=str(i)
    n=len(s)//2 
    if len(s)%2:
        continue
    s1=s[:n]
    for x in s1:
        sum1+=int(x)
 
    s2=s[n:]
    for x in s2:
        sum2+=int(x)
    if sum1==sum2:
        print(i)
    sum1=0
    sum2=0


import math
n=10
res=[]
y = [i*i for i in range(1,n+1)]
print(y)
for i in range(1,11):
    for j in range(1,11):
        x1=i**2 + j**2
        #print(x1)
        if x1 in y:
            
            res.append((i,j,math.sqrt(x1)))
print(len(res))
        #if x1 in y:
            #print(x1)


def countElements(nums):
    l,r=0,len(nums)
    nums.sort()
 
      
    c=r-l
    return c-2

nums = [-71,-71,93,-71,40]
print(countElements(nums))


n=2147483644
res=''
res2='0'*32

while n>0:
    res=str(n%2)+res
    n//=2

n = len(res)
m = 32-n
res='0'*m + res
print(res)
res = res[::-1]
print(res)
num1 = int(res, 2)
print(num1)

""" 
num1 ="9333852702227987"
num2 ="85731737104263"
print(float.__floor__(num1))
print(float(num2))
res = float(num1)+float(num2)
print(res)