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


def canBeIncreasing(nums):
    stack=[]
    s=set()
    for i in nums:
        if not stack:
            stack.append(i)
            s.add(i)
        elif stack[-1]<i and i not in s:
            stack.append(i)
            s.add(i)
        else:
            while stack and stack[-1]>i:
                stack.pop()
            if i not in s:
                stack.append(i)
    if len(stack)>1:
        return True
    else:
        return False

nums = [2,3,1,2]
print(canBeIncreasing(nums))


def moveZeroes(nums):
      
    l,r=0,1

    while r<len(nums):
        if nums[l]==0 and nums[r]!=0:
            nums[l],nums[r]=nums[r],nums[l]
            r+=1
            l+=1
        elif nums[l]==0 and nums[r]==0:
            r+=1
    return nums
nums = [0,1,0,3,12]
print(moveZeroes(nums))

""" 

def wordPattern(pattern, s):
    """
    p=set(pattern)
    p = list(p)
    p.sort()

    #print(p)
    s = s.split()
    #print(s)
    ss=set(s)
    sf = list(ss)
    sf.sort()
    #print(sf)
    
    print(sf)
    d={}
    for i,j in zip(p,sf):
        d[i]=j
    print(d)
    sr=[]
    for i in pattern:
        sr.append(d[i])
    #print(sr)

    if sr == s:
        return True
    else:
        return False

    """

    """
    p=set(pattern) 
    pp=list(p)
    print(len(p)) 
    s=s.split()     
    ss=set(s)
    print(len(ss))
        
      
    if len(pp)==len(ss):
        return True
    else:
        return False

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))




def reverseWords(s):
    res=[]
    
    s = s.split()
    #print(s)
        
    for i in s:
        #print(str(i[::-1]))
        res.append(i[::-1])
    return " ".join(res)

s ="Let's take LeetCode contest"
#print(s[::-1])
print(reverseWords(s))


def reverseStr(s, k):
    n=len(s)
    t=""
    for i in range(0,n,2*k):
        t+=s[i:i+k][::-1] 
        t+=s[i+k:i+2*k]
    return t

s ="abcdefg"
print(reverseStr(s,2))

#print(s[6:8])




def lengthOfLongestSubstring(s):
    c = set()
    n=0
    m=0
    for i in s:
        if i not in c:
            c.add(i)
            n+=1
        else:
            m = max(n,m)
            n=1
    return m

s="abcabcbb"
print(lengthOfLongestSubstring(s))


def reverseWords(s):
    #s = s.replace(" ", ",")
    print(s)
    s=s.split()
    s = s[::-1]
  

    return " ".join(s)

#s = "the sky is blue"
s="the sky is blue"
#s = "a good   example"
print(reverseWords(s))


#mat=[[0,0],[0,1],[1,0],[0,2],[2,0]]
#print(mat[0][1])
#print(mat)

def lengthOfLongestSubstring(s) -> int:
    if s==" ":
        return 1

    if len(s)==1:
        return 1

    c=set()
    n = len(s)
    ma = 0
    x=0
    for i in range(n-1):
        while s[i] in c:
            c.remove(s[x])
            x+=1
        c.add(s[i])
        ma = max(ma,i-x+1)
    return ma
    
s="au"
print(lengthOfLongestSubstring(s))



s = ["flower","flow","flight"]
mi = min(s)
ma = max(s)
print(mi)
print(ma)


def sub(s):
    n=0
    res=[]
    c=0
    while n<len(s)-2:
        print(s[n:n+3])
        if "OOO" in s[n:n+3]:
            n+=1
        else:
            c+=1
            n+=1
    return c

#s = "XXOX"
#s="OOOO"
s="XXX"
print(sub(s))


def isMonotonic(nums):
    f = [True if nums[0]<nums[-1] else False]
    if f[0]:
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]<=nums[j]:
                continue
            else:
                return False
    else:
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]>=nums[j]:
                continue
            else:
                return False
    return True

nums = [6,5,4,4]
print(isMonotonic(nums))


from collections import Counter
import heapq
def topFeq(nums, k):
    c = Counter(nums)
    heap=[]

    for key,val in c.items():
        if len(heap)<k:
            heapq.heappush(heap, (val,key))
        else:
            heapq.heappushpop(heap, (val,key))
    h=[h[1] for h in heap]
    return h
nums = [1,1,1,2,2,3]
print(topFeq(nums, 2))


def multiply(num1,num2):
    if "0" in [num1, num2]:
        return "0"
    
    res = [0] * (len(num1) + len(num2))
    num1, num2 = num1[::-1], num2[::-1]
    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            digit = int(num1[i1]) * int(num2[i2])
            res[i1 + i2] += digit
            res[i1 + i2 + 1] += res[i1 + i2] // 10
            res[i1 + i2] = res[i1 + i2] % 10

    res, beg = res[::-1], 0
    while beg < len(res) and res[beg] == 0:
        beg += 1
    res = map(str, res[beg:])
    return "".join(res)

num1 = "123"
num2 = "456"
print(multiply(num1,num2))

from collections import Counter
def wordBreak(s, wordDict):
    maxlen=0
    wordset = set(wordDict)
    print(wordset)
    for word in wordDict:
        maxlen=max(maxlen, len(word))
    n = len(s)
    dp = [0]*(n+1)
    dp[0]=True
    #print(dp) print(maxlen)  
    for i in range(1, n+1):
        for j in range(i - 1, max(0, i - maxlen) - 1, -1):        
            if dp[j] and s[j:i] in wordset:
                dp[i]=True
                break
    print(dp)
    return dp[n]

         
   
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
#s="leetcode"
#wordDict=["leet","code"]
#s = "applepenapple"
#wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))


def hindex(citations):
    n=len(citations)
    pc=[0]*(n+1)

    for c in citations:
        pc[min(n,c)]+=1
    h=n
    papers=pc[n]

    while papers<h:
        h-=1
        papers+=pc[h]

    return h
citations = [3,0,6,1,5]
print(hindex(citations))


def trap(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
"""
"""
from collections import Counter
def topKFrequent(nums,k):
    n = len(nums)
    counter = Counter(nums)
    buckets = [0] * (n + 1)

    for num, freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num]
        else:
            buckets[freq].append(num)
        
    ret = []
    for i in range(n, -1, -1):
        if buckets[i] != 0:
            ret.extend(buckets[i])
        if len(ret) == k:
            break
      
    return ret
nums = [1,1,1,2,2,3,3,3]
k = 2
print(topKFrequent(nums,k))


def trap(height):
       
    n = len(height)
    l_max = [0] * n
    r_max = [0] * n

    l_max[0] = height[0]
    r_max[-1] = height[-1]

    result = 0
    for l in range(1, n):
        l_max[l] = max(l_max[l-1], height[l])

    for r in range(n-2, -1, -1):
        r_max[r] = max(r_max[r+1], height[r])

    for i in range(1, n-1):
        result += min(l_max[i], r_max[i]) - height[i]
       
    return result

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))



def triangle(numRows):

    triangle=[[1]]
  
    for i in range(numRows-1):
        res=[]
        temp = [0]+triangle[-1]+[0]
        for x in range(len(triangle[-1])+1):
            res.append(temp[x]+temp[x+1])

        triangle.append(res)

    return triangle

numRows = 5
print(triangle(numRows))
"""
"""
def mono(nums):
    c1=0
    c2=0

    for i in range(len(nums)-1):
        if nums[i]<=nums[i+1]:
            c1+=1
        if nums[i]>=nums[i+1]:
            c2+=1
     
    if c1==len(nums)-1 or c2==len(nums)-1:
        return True
    else:
        return False

nums=[1,2,2,3]
#nums=[5,7,4,2,1]
print(mono(nums))

def numIdenticalPairs(nums):
    c=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                c+=1
    return c

nums =[1,2,3,1,1,3]
print(numIdenticalPairs(nums))

def generate(numRows):
    triangle=[[1]]     
    
    for x in range(numRows-1):  
        res=[]      
        tem=[0]+triangle[-1]+[0]  
        for i in range(len(triangle[-1])+1):            
            res.append(tem[i]+tem[i+1])
        triangle.append(res)
              
    return triangle[4]
numRows = 5
print(generate(numRows))

def romantoint(s):
    d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    i=0
    res=0
    while i < len(s):
        if i<len(s)-1 and d[s[i]]<d[s[i+1]]:
            res+=d[s[i+1]]-d[s[i]]
            i+=2
        
        else:
            res+=d[s[i]]
            i+=1
    return res  
s = "III"  
#s = "MCMXCIV"
print(romantoint(s))


def mySqrt(x):
    l=0
    r=x
    res=0
    if x==1:
        return 1
    while l<=r:
         
        m=l+((r-l)//2)

        if m**m>x:
            r=m-1                
        elif m**m<x:
            l=m+1  
            res=m            
        else:
            return m
    return res
x=9
y=9
if x>y:
    print("hello")       
n=9
print(mySqrt(n))

def arraySign(nums):
    l,r=0,len(nums)-1
    c=0
    while l<=r:
        if nums[l] == 0 or nums[r]==0:
            return 0
        if nums[l]<0:
            c+=1
        if nums[r]<0:
            c+=1  
        if nums[r]==nums[l]:
            c-=1          
        l+=1
        r-=1
    if c%2==0:
        return 1
    else:
        return -1
#nums = [-1,-2,-3,-4,3,2,1]
nums = [-1,1,-1,1,-1]
print(arraySign(nums))
            
"""

for i in range(-16):
    print(i)
import math
print(math.sqrt(-16))