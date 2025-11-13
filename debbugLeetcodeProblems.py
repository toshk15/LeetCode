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
            


def flipAndInvertImage(image):
    row = len(image)
    col = len(image[0])

    for i in range(row):
        image[i][:]=[image[i][::-1]]
        for j in range(col):
            
            if image[i][j]==1:
                image[i][j]=0
            else:
                image[i][j]=1
    return image

res2=[]
image = [[1,1,0],[1,0,1],[0,0,0]]
for x in image:
    res1=[]
    for y in x:
        if y==1:
            y=0
        else:
            y=1
        res1.append(y)
    res2.append([res1[::-1]])

print(res2)
#print(flipAndInvertImage(image))


words = ["bella","label","roller"]
from collections import Counter
r=[]
for c in words:
    r.append(Counter(c))
print(r)
aux=r[0]
for i in range(1,len(r)):
    aux&=r[i]
print(aux)
res=[]
for i, j in aux.items():
    res.append(i*j)
res= "".join(res)

r=[]
for i in res:
    r+=i
print(r)

def findMissingAndRepeatedValues(grid):
    row=len(grid)
    col=len(grid[0])
    n=row*col

    s = set()
    for i in range(1,n+1):
        s.add(i)

    for i in range(row):
        for j in range(col):
            if grid[i][j] in s:
                s.remove(grid[i][j])
            else:
                s.add(grid[i][j])
    return list(s)


#grid = [[1,3],[2,2]]
grid = [[9,1,7],[8,9,2],[3,4,6]]
print(findMissingAndRepeatedValues(grid))


def maxDistance(arrays):
    maximum = arrays[0][-1]
    minimum = arrays[0][0]
    s3=float("-inf")

    for n in range(1,len(arrays)):
        s1=maximum-arrays[n][0]
        s2=arrays[n][-1]-minimum
        maximum=max(maximum,arrays[n][-1])
        minimum=min(minimum,arrays[n][0])
        s3=max(s3,s1,s2)

    return s3

arrays=[[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
print(maxDistance(arrays))


def lemonadeChange(bills):
    five=0
    ten=0
    twenty=0

    for c in bills:
        if c==5:
            five+=1             
        if c==10:
            ten+=1
            five-=1
            if five<0:
                return False
        if c==20:
            twenty+=1                
            if ten<=0 and five<=0:
                return False
            elif ten<=0 and five>=3:
                five-=3                   
            else:
                ten-=1
                five-=1
        
    return True

bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print(lemonadeChange(bills))


def findContentChildren(g,s):
    g.sort()
    s.sort()
    l=r=0
    c=0

    while l<len(s):
        if l<len(s) and r<len(g) and s[l]>=g[r]:
            l+=1
            r+=1
            c+=1
        elif l==len(s):
            break
        else:
            l+=1
    return c

#g = [1,2,3]
#s = [1,1]

g = [1,2]
s = [1,2,3]
print(findContentChildren(g,s))



def canPlaceFlowers(flowerbed, n):
    flowerbed = [0]+flowerbed+[0]
    for i in range(1,len(flowerbed)):
        
        if i+1<len(flowerbed) and flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
            flowerbed[i]=1
            n-=1
    return True if n==0 else False

    
#flowerbed = [1,0,0,0,0,1]
flowerbed = [0,0,1,0,1]
#flowerbed = [0,1,0] #[0,0,1,0,0]
n=1
print(canPlaceFlowers(flowerbed,n))
"""
"""
def matrix(mat):
    if not mat or not mat[0]:
        return []
    R,C=len(mat), len(mat[0])
    result=[]
    row, col = 0,0
    dir=1

    while len(result)<R*C:
        result.append(mat[row][col])

        if dir==1:
            if col==C-1:
                row+=1
                dir=-1
            elif row==0:
                col+=1
                dir=-1
            else:
                row-=1
                col+=1
        else:
            if row==R-1:
                col+=1
                dir=1
            elif col==0:
                row+=1
                dir=1
            else:
                row+=1
                col-=1
    return result

"""

"""
from collections import defaultdict
def isToeplitzMatrix(matrix):
    d = defaultdict(list)
    R=len(matrix)
    C=len(matrix[0])
    for i in range(R):
        for j in range(C):
            d[i-j].append(matrix[i][j])
       
    for o in d.values():
        o=set(o)
        if len(o)==1:
            continue
        else:
            return False
    return True
m=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(isToeplitzMatrix(m))


from collections import defaultdict
def matrix(mat):
    if not mat or not mat[0]:
        return []
    
    R,C=len(mat),len(mat[0])
    dia =defaultdict(list)

    for i in range(R):
        for j in range(C):
            dia[i+j].append(mat[i][j])

    result=[]

    for i in dia.values():
        print(i)
        i = set(i)
        print(i)

    for i in range(R+C-1):
        if i%2==0:
            dia[i].reverse()

        result.extend(dia[i])
    
    return result
    


mat = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(matrix(mat))


def modifiedMatrix(matrix): 
    R=len(matrix)
    C=len(matrix[0])   
    for i in range(R):
        for j in range(C):
            if matrix[i][j]==-1:
                m=findGreatest(i,j,R)
                matrix[i][j]=m 
    return matrix   

def findGreatest(i,j,R):
    m=float("-inf")
    while i<R:
        m = max(m,matrix[i][j])
        i+=1
    return m
    



matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
print(modifiedMatrix(matrix))


def nextGreaterElement(nums1,nums2):
    m = 0 
    res=[]
    for n in nums1:
        index=nums2.index(n)
        for nn in nums2[index:]:
            if nn>n:
                m=nn
                break
            else:
                m=-1
        res.append(m)

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))


def findLUSlength(a, b):
    c=0
    la=len(a)
    lb=len(b)
    
    for i,j in zip(a,b):
        print(i,j)
        if i!=j:
            c+=1
    return -1 if c==0 else c
                    
                
a = "aefawfawfawfaw"
b = "aefawfeawfwafwaef"            
#a = "aba"
#b = "cdc"
print(findLUSlength(a,b))

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss=s+s
        
        if s in ss[1:-1]:
            return True
        else:
            return False

s = "abab"
print(repeatedSubstringPattern(s))



def search(nums,target):
    l=0
    r=len(nums)

    while l<=r:
        m=l+(r-l)//2

        if nums[m]==target:
            return m
        if nums[m]<target:
            l=m+1
        else:
            r=m-1
    return -1

#ums = [-1,0,3,5,9,12]
nums = [-1,0,3,5,9,12]
target=13
print(search(nums, target))


num=[1,2,3,4]
num="".join(map(str,num))
print(num)


def validPalindrome(s):
    l=0
    r=len(s)-1
    while l<=r:
        if s[l]!=s[r]:
            print(s[l+1:r+1])
            print(s[l+1:r+1][::-1])
            print(s[l:r])
            print(s[l:r][::-1])
            if s[l+1:r+1]==s[l+1:r+1][::-1] or s[l:r]==s[l:r][::-1]:
                return True 
            else:
                return False
                     
        l+=1
        r-=1
        if r<=l:
            return True
     
    return False

s ="abc"
print(validPalindrome(s))


def minimumLength(s):
    l = 0
    r = len(s)-1
    if len(s)==1:
        return 1
    while l<r:
        while l<len(s)-1 and s[l]==s[r]:
            l+=1
        while r>1 and l>=1 and s[l-1]==s[r]:
            if r<l:
                return 0
            r-=1   
        
        if s[l]!=s[r] or l==r:
            return r-l+1
    return 0

#s="aabaaa"
        
#s = "aabccabba"
#s = "cabaabac"
#s="bbbbbbbbbbbbbbbbbbb"
s="abbbbbbbbbbbbbbbbbbba"
print(minimumLength(s))


def waysToSplitArray(nums):
    s = sum(nums)
    v=0
    res=0
    for i in range(len(nums)-1):
        v+=nums[i]
        s-=nums[i]            
        if v>=s:
            res+=1
    return res

nums = [10,4,-8,7]
print(waysToSplitArray(nums))


from collections import Counter
def relativeSortArray(arr1, arr2):
    c = Counter(arr1)
    res=[]
    res2=[]
    for i in arr2:
        while c[i]>0:
            res.append(i)
            c[i]-=1
        del c[i]
    for i in c:
        while c[i]>0:
            res2.append(i)
            c[i]-=1
    
    return res+sorted(res2)

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSortArray(arr1, arr2))


def maxWidthOfVerticalArea(points):
    points=sorted(points, key=lambda point:point[0])
    m=float("-inf")
    for i in range(1,len(points)):
        ma= points[i][0]- points[i-1][0]
        m=max(m,ma)
    return m

points =[[8,7],[9,9],[7,4],[9,7]]
print(maxWidthOfVerticalArea(points))


def maxScore(s):
    zeros=0
    ones=s.count("1")
    res=0

    for i in range(len(s)-1):
        if s[i]=="0":
            zeros+=1
        if s[i]=="1":
            ones-=1
        res=max(res,ones+zeros)
    return res
s = "011101"
print(maxScore(s))

from collections import Counter
def permuteUnique(nums):
    c = Counter(nums)
    comb=[]
    res=[]

    def backtrack():
        if len(comb)==len(nums):
            res.append(comb[:])                
            
        for n in c:
            if c[n]==0:
                continue
            comb.append(n)
            c[n]-=1
            backtrack()
            comb.pop()
            c[n]+=1
    backtrack()
    return res 

nums = [1,1,2]
print(permuteUnique(nums))


def carFleet(target, position, speed):
    res=zip(position,speed)
    res=sorted(res,reverse=True)
    c=1
    u,v = res[0]
    t=(target-u)/v
    
    for i,j in res:
        x = (target-i)/j
        if x<=t:
            continue
        else:
            c+=1
            t=x
    return c
            

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(carFleet(target, position, speed))


def imageSmoother(img):
    row = len(img)
    col = len(img[0])
    res=[[0]*col for n in range(row)]

    for i in range(row):
        for j in range(col):
            s=0
            c=0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if ii<0 or ii==row or jj<0 or jj==col:
                        continue
                    s+=img[ii][jj]
                    c+=1
            res[i][j]=s//c
    return res


img = [[100,200,100],[200,50,200],[100,200,100]]
print(imageSmoother(img))


if 0<0:
    print("TRUE")
else:
    print("FALSE")

    

def reverseOnlyLetters(s):        
    s=list(s)
    l=0
    r=len(s)-1
    while l<r:
        if s[l].isalpha() and s[r].isalpha():
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        elif not s[l].isalpha():
            l+=1
        elif not s[r].isalpha():
            r-=1
    return "".join(s)
            
s = "ab-cd"
print(reverseOnlyLetters(s))


def letterCombinations(digits):
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        for c in digitToChar[digits[i]]:
            backtrack(i + 1, curStr + c)

    if digits:
        backtrack(0, "")

    return res

digits = "23"
print(letterCombinations(digits))



def partition(s):
    part=[]
    res=[]

    def pali(s,i,x):
        while i<=x:
            if s[i]!=s[x]:
                return False
            i+=1
            x-=1
        return True

    def dfs(i):
        if i >= len(s):
            res.append(part[:])
            return
            
        for x in range(i, len(s)):
            if pali(s,i,x):
                part.append(s[i:x+1])
                dfs(x+1)
                part.pop()
    dfs(0)
    return res

s = "aab"
print(partition(s))


from collections import Counter
def frequencySort(nums):
    c = Counter(nums)  
    res=[]
    res2=[]
    for n in c:
        res.append((c[n],-n))
    res=sorted(res)
    print(res)
    for i,j in res:
        while i>0:
            res2.append(-j)
            i-=1
    return res2  


nums = [-1,1,-6,4,5,-6,1,4,1]
print(frequencySort(nums))



def splitString(s):
    def dfs(index,prev):
        if index==len(s):
            return True
        
        for i in range(index, len(s)):
            val = int(s[index:i+1])
            if val+1==prev and dfs(i+1,val):
                return True
        return False
    
    for start in range(len(s)-1):
        val=int(s[:start+1])
        if dfs(start+1,val):
            return True
    return False
s = "050043"
print(splitString(s))


def simplifyPath(path):
    stack = []
    path = path.split("/")
    for p in path:
        if stack and p == "..": # pop stack if non-empty
            stack.pop()
            continue

        if p not in [".", "/", "", ".."]:
            # Ignore the "p" which are no-op, 
            # but also ".." in case the stack was in previous condition. Example: "/../"
            stack.append(p)
        
    return "/" + "/".join(stack)

path ="/home///foo/"
#path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))



def search(nums, target):
    l=0
    r=len(nums)-1

    while l<r:
        m=(l+r)//2

        if nums[m]>nums[r]:
            l=m+1          
        else:
            r=m
    mid=l

    if mid==0:
        l=0
        r=len(nums)-1
    elif target>=nums[0] and target<=nums[mid-1]:
        l=0
        r=mid-1
    else:
        l=mid
        r=len(nums)-1

    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            return m
        elif target<nums[m]:
            r=m-1
        else:
            l=m+1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))

def divideArray(nums,k):
    nums.sort()
    res=[]
    for i in range(0, len(nums), 3):
        if nums[i+2]-nums[i]<=k:
            res.append([nums[i], nums[i+1],nums[i+2]])
    return res

nums = [2,4,2,2,5,2]
k = 2
print(divideArray(nums,k))

from collections import Counter
def findEvenNumbers(digits):
    dc=Counter(digits)
    res=[]

    for n in range(100,999,2):
        n=str(n)
        nc=Counter(n)
        F=True
        for i,j in nc.items():
            if dc[int(i)]<j:                    
                F=False
                break
        if F:
            res.append(n)
    return res

digits = [2,1,3,0]
print(findEvenNumbers(digits))

from collections import defaultdict
def isValidSudoku(board):
    rows=defaultdict(set)
    cols=defaultdict(set)
    boxes=defaultdict(set)

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue

            box_key = (r//3,c//3)

            if num in rows or num in cols or num in boxes[box_key]:
                return False
            
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_key].add(num)
    return True



board =[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

print(isValidSudoku(board))

print(1//3)



def candy(ratings):
    res=[1]*len(ratings)

    for i in range(1,len(ratings)):
        if ratings[i]>ratings[i-1]:
            res[i]=res[i-1]+1
    for i in range(len(ratings)-1,-1,-1):
        if i>0 and ratings[i]<ratings[i-1]:
            if res[i]<res[i-1]:
                continue
            else:
                res[i-1]=res[i]+1
    return sum(res)



ratings = [1,0,2]
print(candy(ratings))

def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()
    start, end = intervals[0]
    res=[]
    for s,e in intervals[1:]:
        if end>=s:
            start=min(start,s)
            end=max(end, e)
        else:
            res.append([start, end]) 
            start,end=s,e  
    res.append([start,end])        
    return res
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))


def maxProfit(prices):
    maxprofit=0
    buyprice=prices[0]
    res=[]
    for p in prices[1:]:
        if p<buyprice:
            buyprice=p
        else:
            currprofit = p-buyprice
            maxprofit=max(currprofit, maxprofit)
            res.append(maxprofit)
            maxprofit=0
            buyprice=p
    print(res)
    return sum(res)
prices = [7,1,5,3,6,4]
print(maxProfit(prices))





def minOPeration(nums):
    s=[]
    res=0
    for n in nums:
        while s and s[-1]>n:
            s.pop()

        if n==0:
            continue

        if not s or s[-1]<n:
            res+=1
            s.append(n)
    return res

#nums = [1,2,1,2,1,2]
nums = [4,3,4,6]
print(minOPeration(nums))



def digitSum(s, k):    

    while len(s)>k:
        ss=""
        sf=""
        i=0      

        while i < len(s):
            sm=0
            ss=s[i:i+k]
            for ii in ss:
                sm+=int(ii)
            sf+=str(sm)
            i+=k
        s=sf
    return s
       

s = "11111222223"
k = 3

print(digitSum(s, k))



def findRestaurant(list1,list2):
    idx=float("inf")
    res=[]
    for c in list1:            
        if c in list2:
            index1=list1.index(c)
            index2=list2.index(c)
            totalidx=index1+index2
            if totalidx<=idx:
                idx=totalidx
                res.append([c,idx])
    x=min(res)
    print(x[1])
  
    res2=[]
    for i,j in res:
        if j==x[1]:
            res2.append(i)
    #print(x)
    return res2

#list1 = ["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

#list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(findRestaurant(list1,list2))



def minDeletionSize(strs):
    cols = len(strs[0])
    rows=len(strs)
    m = [[0]*cols for i in range(rows)]
    for i in range(len(strs)):
        for j in range(len(strs[i])):
            m[i][j]= strs[i][j]
    print(m)
   
    c=0
    
    for j in range(cols):
            i=1
            while i<rows:
                print(m[i-1][j])
                print(m[i][j])
                if i<rows and m[i-1][j]<m[i][j]:
                    i+=1
                else:
                    c+=1
                    i+=1
                    break
    return c
   

strs = ["cba","daf","ghi"]
#strs = ["a","b"]
#strs = ["zyx","wvu","tsr"]
print(minDeletionSize(strs))

if "a"<"b":
     print("yes")
else:
     print("no")
"""
"""
def duplicateZeros(arr):
    n = len(arr)
    zeros = arr.count(0)

    i=n-1
    j=n+zeros-1

    while i < j:
        if j<n:
            arr[j]=arr[i]
        
        if arr[i]==0:
            j-=1
            if j<n:
                arr[j]=0
        i-=1
        j-=1

def duplicateZeros(arr):
    ss=""
    for i in arr:
        if i!=0:
            ss+=str(i)
        elif i==0:
            ss+="00"
    i=0
    while i<len(arr):
        print(ss[i])
        arr[i]=int(ss[i])
        i+=1
                

arr = [1,0,2,3,0,4,5,0]
print(duplicateZeros(arr))

"""

def eraseOverlapIntervals(intervals):
    intervals.sort()
    start, end = intervals[0]
    res=0
    for start_new, end_new in intervals[1:]:
        if start_new>=end:
            end=end_new
        else:
            res+=1
            end=min(end,end_new)
    return res
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))