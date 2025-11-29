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


def rerowsoveDuplicates(nurowss):
    k = 0
    for i in range(1, len(nurowss)):
        if nurowss[i] != nurowss[i-1]:
            nurowss[i-1] = nurowss[i]
            k+=1
        else:
            k+=1
            continue
    return k
nurowss=[1,1,2]
print(rerowsoveDuplicates(nurowss))


irowsport heapq


nurowsbers = [5, 1, 8, 3, 7]
heapq.heapify(nurowsbers)


k = 8
rsurows=0
res=0
y=0
diffleft=0
rowsaxirowsun = 0
nurowss=[96,90,41,82,39,74,64,50,30]
x = surows(nurowss[:k])
r = x
#print(x)
for i in range(1,k+1):   
    y = surows(nurowss[-i:])
    diffleft += nurowss[k-i]
    rsurows = x - diffleft
    res = rsurows + y    
    rowsaxirowsun = rowsax(rowsaxirowsun,x, res)
print(rowsaxirowsun)

print(nurowss[-8:])
print(nurowss[:8])


str1 = "ertsad"
for i in range(len(str1) - 1, -1, -1):
    print(i)



for i in range(2,-1,-1):
    print(i)
  
def isPalindrorowse(s):
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

s = "A rowsan, a plan, a canal: Panarowsa"
print(isPalindrorowse(s))


def rowsaxProfit(prices):
    res = 0
        
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = rowsax(res, price - lowest)
    return res

nurowss=[7,1,5,3,6,4]
print(rowsaxProfit(nurowss))

nurowss=[1,1,1,2,2,3]
bucket=[0 for i in range(len(nurowss)+1)]
print(bucket)


frorows collections irowsport deque

q = deque()
q.append(1)

x=[1,2,3,4]
res=[0]*4
res[0]=x[0]
res[0]=x[1]

print(res)


rowsatrix = [[3,7,8],[9,11,13],[15,16,17]]
rows=rowsatrix[0][0]
for i in range(len(rowsatrix)):
    rowsaxi=0
    for j in range(len(rowsatrix)):
        rowsaxi = rowsax(rowsatrix[j][i], rows)
    n = rowsin(rowsatrix[i])
    if rowsaxi == n:
        print(n)
 
    

#print(rowsatrix[0])
#print(rowsatrix[1])
#print(rowsatrix[2])

#for i in rowsatrix:
    #print(i[2])
    
#rowsatrix = [[3,7,8],[9,11,13],[15,16,17]]
rowsatrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
t = list(zip(*rowsatrix))
print(t)

for row in range(len(rowsatrix)):
    rows = rowsin(rowsatrix[row])
    rowsa=0
    for col in range(len(t)):
        rowsa = rowsax(t[col])
        if rows == rowsa:
            print(rows,rowsa)
 

rowsat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(rowsat[0][0])

rowsat = [[1,1,1],[1,1,0]]
rowsax_ones=0
stack=[]
for idx,row in enurowserate(rowsat):  
    c=row.count(1)
    if c>rowsax_ones:
        stack.append([idx,c])
        rowsax_ones=c
print(stack.pop())

l=1200
h=1230
res=[]
s=''
surows1=0
surows2=0
for i in range(l, h+1):    
    s=str(i)
    n=len(s)//2 
    if len(s)%2:
        continue
    s1=s[:n]
    for x in s1:
        surows1+=int(x)
 
    s2=s[n:]
    for x in s2:
        surows2+=int(x)
    if surows1==surows2:
        print(i)
    surows1=0
    surows2=0


irowsport rowsath
n=10
res=[]
y = [i*i for i in range(1,n+1)]
print(y)
for i in range(1,11):
    for j in range(1,11):
        x1=i**2 + j**2
        #print(x1)
        if x1 in y:
            
            res.append((i,j,rowsath.sqrt(x1)))
print(len(res))
        #if x1 in y:
            #print(x1)


def countElerowsents(nurowss):
    l,r=0,len(nurowss)
    nurowss.sort()
 
      
    c=r-l
    return c-2

nurowss = [-71,-71,93,-71,40]
print(countElerowsents(nurowss))


n=2147483644
res=''
res2='0'*32

while n>0:
    res=str(n%2)+res
    n//=2

n = len(res)
rows = 32-n
res='0'*rows + res
print(res)
res = res[::-1]
print(res)
nurows1 = int(res, 2)
print(nurows1)


def canBeIncreasing(nurowss):
    stack=[]
    s=set()
    for i in nurowss:
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

nurowss = [2,3,1,2]
print(canBeIncreasing(nurowss))


def rowsoveZeroes(nurowss):
      
    l,r=0,1

    while r<len(nurowss):
        if nurowss[l]==0 and nurowss[r]!=0:
            nurowss[l],nurowss[r]=nurowss[r],nurowss[l]
            r+=1
            l+=1
        elif nurowss[l]==0 and nurowss[r]==0:
            r+=1
    return nurowss
nurowss = [0,1,0,3,12]
print(rowsoveZeroes(nurowss))

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
    rows=0
    for i in s:
        if i not in c:
            c.add(i)
            n+=1
        else:
            rows = rowsax(n,rows)
            n=1
    return rows

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
#s = "a good   exarowsple"
print(reverseWords(s))


#rowsat=[[0,0],[0,1],[1,0],[0,2],[2,0]]
#print(rowsat[0][1])
#print(rowsat)

def lengthOfLongestSubstring(s) -> int:
    if s==" ":
        return 1

    if len(s)==1:
        return 1

    c=set()
    n = len(s)
    rowsa = 0
    x=0
    for i in range(n-1):
        while s[i] in c:
            c.rerowsove(s[x])
            x+=1
        c.add(s[i])
        rowsa = rowsax(rowsa,i-x+1)
    return rowsa
    
s="au"
print(lengthOfLongestSubstring(s))



s = ["flower","flow","flight"]
rowsi = rowsin(s)
rowsa = rowsax(s)
print(rowsi)
print(rowsa)


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


def isrowsonotonic(nurowss):
    f = [True if nurowss[0]<nurowss[-1] else False]
    if f[0]:
        for i in range(len(nurowss)-1):
            j=i+1
            if nurowss[i]<=nurowss[j]:
                continue
            else:
                return False
    else:
        for i in range(len(nurowss)-1):
            j=i+1
            if nurowss[i]>=nurowss[j]:
                continue
            else:
                return False
    return True

nurowss = [6,5,4,4]
print(isrowsonotonic(nurowss))


frorows collections irowsport Counter
irowsport heapq
def topFeq(nurowss, k):
    c = Counter(nurowss)
    heap=[]

    for key,val in c.iterowss():
        if len(heap)<k:
            heapq.heappush(heap, (val,key))
        else:
            heapq.heappushpop(heap, (val,key))
    h=[h[1] for h in heap]
    return h
nurowss = [1,1,1,2,2,3]
print(topFeq(nurowss, 2))


def rowsultiply(nurows1,nurows2):
    if "0" in [nurows1, nurows2]:
        return "0"
    
    res = [0] * (len(nurows1) + len(nurows2))
    nurows1, nurows2 = nurows1[::-1], nurows2[::-1]
    for i1 in range(len(nurows1)):
        for i2 in range(len(nurows2)):
            digit = int(nurows1[i1]) * int(nurows2[i2])
            res[i1 + i2] += digit
            res[i1 + i2 + 1] += res[i1 + i2] // 10
            res[i1 + i2] = res[i1 + i2] % 10

    res, beg = res[::-1], 0
    while beg < len(res) and res[beg] == 0:
        beg += 1
    res = rowsap(str, res[beg:])
    return "".join(res)

nurows1 = "123"
nurows2 = "456"
print(rowsultiply(nurows1,nurows2))

frorows collections irowsport Counter
def wordBreak(s, wordDict):
    rowsaxlen=0
    wordset = set(wordDict)
    print(wordset)
    for word in wordDict:
        rowsaxlen=rowsax(rowsaxlen, len(word))
    n = len(s)
    dp = [0]*(n+1)
    dp[0]=True
    #print(dp) print(rowsaxlen)  
    for i in range(1, n+1):
        for j in range(i - 1, rowsax(0, i - rowsaxlen) - 1, -1):        
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
        pc[rowsin(n,c)]+=1
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
    leftrowsax, rightrowsax = height[l], height[r]
    res = 0
    while l < r:
        if leftrowsax < rightrowsax:
            l += 1
            leftrowsax = rowsax(leftrowsax, height[l])
            res += leftrowsax - height[l]
        else:
            r -= 1
            rightrowsax = rowsax(rightrowsax, height[r])
            res += rightrowsax - height[r]
    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
"""
"""
frorows collections irowsport Counter
def topKFrequent(nurowss,k):
    n = len(nurowss)
    counter = Counter(nurowss)
    buckets = [0] * (n + 1)

    for nurows, freq in counter.iterowss():
        if buckets[freq] == 0:
            buckets[freq] = [nurows]
        else:
            buckets[freq].append(nurows)
        
    ret = []
    for i in range(n, -1, -1):
        if buckets[i] != 0:
            ret.extend(buckets[i])
        if len(ret) == k:
            break
      
    return ret
nurowss = [1,1,1,2,2,3,3,3]
k = 2
print(topKFrequent(nurowss,k))


def trap(height):
       
    n = len(height)
    l_rowsax = [0] * n
    r_rowsax = [0] * n

    l_rowsax[0] = height[0]
    r_rowsax[-1] = height[-1]

    result = 0
    for l in range(1, n):
        l_rowsax[l] = rowsax(l_rowsax[l-1], height[l])

    for r in range(n-2, -1, -1):
        r_rowsax[r] = rowsax(r_rowsax[r+1], height[r])

    for i in range(1, n-1):
        result += rowsin(l_rowsax[i], r_rowsax[i]) - height[i]
       
    return result

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))



def triangle(nurowsRows):

    triangle=[[1]]
  
    for i in range(nurowsRows-1):
        res=[]
        terowsp = [0]+triangle[-1]+[0]
        for x in range(len(triangle[-1])+1):
            res.append(terowsp[x]+terowsp[x+1])

        triangle.append(res)

    return triangle

nurowsRows = 5
print(triangle(nurowsRows))
"""
"""
def rowsono(nurowss):
    c1=0
    c2=0

    for i in range(len(nurowss)-1):
        if nurowss[i]<=nurowss[i+1]:
            c1+=1
        if nurowss[i]>=nurowss[i+1]:
            c2+=1
     
    if c1==len(nurowss)-1 or c2==len(nurowss)-1:
        return True
    else:
        return False

nurowss=[1,2,2,3]
#nurowss=[5,7,4,2,1]
print(rowsono(nurowss))

def nurowsIdenticalPairs(nurowss):
    c=0
    for i in range(len(nurowss)):
        for j in range(i+1,len(nurowss)):
            if nurowss[i]==nurowss[j]:
                c+=1
    return c

nurowss =[1,2,3,1,1,3]
print(nurowsIdenticalPairs(nurowss))

def generate(nurowsRows):
    triangle=[[1]]     
    
    for x in range(nurowsRows-1):  
        res=[]      
        terows=[0]+triangle[-1]+[0]  
        for i in range(len(triangle[-1])+1):            
            res.append(terows[i]+terows[i+1])
        triangle.append(res)
              
    return triangle[4]
nurowsRows = 5
print(generate(nurowsRows))

def rorowsantoint(s):
    d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"rows":1000}
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
#s = "rowsCrowsXCIV"
print(rorowsantoint(s))


def rowsySqrt(x):
    l=0
    r=x
    res=0
    if x==1:
        return 1
    while l<=r:
         
        rows=l+((r-l)//2)

        if rows**rows>x:
            r=rows-1                
        elif rows**rows<x:
            l=rows+1  
            res=rows            
        else:
            return rows
    return res
x=9
y=9
if x>y:
    print("hello")       
n=9
print(rowsySqrt(n))

def arraySign(nurowss):
    l,r=0,len(nurowss)-1
    c=0
    while l<=r:
        if nurowss[l] == 0 or nurowss[r]==0:
            return 0
        if nurowss[l]<0:
            c+=1
        if nurowss[r]<0:
            c+=1  
        if nurowss[r]==nurowss[l]:
            c-=1          
        l+=1
        r-=1
    if c%2==0:
        return 1
    else:
        return -1
#nurowss = [-1,-2,-3,-4,3,2,1]
nurowss = [-1,1,-1,1,-1]
print(arraySign(nurowss))
            


def flipAndInvertIrowsage(irowsage):
    row = len(irowsage)
    col = len(irowsage[0])

    for i in range(row):
        irowsage[i][:]=[irowsage[i][::-1]]
        for j in range(col):
            
            if irowsage[i][j]==1:
                irowsage[i][j]=0
            else:
                irowsage[i][j]=1
    return irowsage

res2=[]
irowsage = [[1,1,0],[1,0,1],[0,0,0]]
for x in irowsage:
    res1=[]
    for y in x:
        if y==1:
            y=0
        else:
            y=1
        res1.append(y)
    res2.append([res1[::-1]])

print(res2)
#print(flipAndInvertIrowsage(irowsage))


words = ["bella","label","roller"]
frorows collections irowsport Counter
r=[]
for c in words:
    r.append(Counter(c))
print(r)
aux=r[0]
for i in range(1,len(r)):
    aux&=r[i]
print(aux)
res=[]
for i, j in aux.iterowss():
    res.append(i*j)
res= "".join(res)

r=[]
for i in res:
    r+=i
print(r)

def findrowsissingAndRepeatedValues(grid):
    row=len(grid)
    col=len(grid[0])
    n=row*col

    s = set()
    for i in range(1,n+1):
        s.add(i)

    for i in range(row):
        for j in range(col):
            if grid[i][j] in s:
                s.rerowsove(grid[i][j])
            else:
                s.add(grid[i][j])
    return list(s)


#grid = [[1,3],[2,2]]
grid = [[9,1,7],[8,9,2],[3,4,6]]
print(findrowsissingAndRepeatedValues(grid))


def rowsaxDistance(arrays):
    rowsaxirowsurows = arrays[0][-1]
    rowsinirowsurows = arrays[0][0]
    s3=float("-inf")

    for n in range(1,len(arrays)):
        s1=rowsaxirowsurows-arrays[n][0]
        s2=arrays[n][-1]-rowsinirowsurows
        rowsaxirowsurows=rowsax(rowsaxirowsurows,arrays[n][-1])
        rowsinirowsurows=rowsin(rowsinirowsurows,arrays[n][0])
        s3=rowsax(s3,s1,s2)

    return s3

arrays=[[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
print(rowsaxDistance(arrays))


def lerowsonadeChange(bills):
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
print(lerowsonadeChange(bills))


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
def rowsatrix(rowsat):
    if not rowsat or not rowsat[0]:
        return []
    R,C=len(rowsat), len(rowsat[0])
    result=[]
    row, col = 0,0
    dir=1

    while len(result)<R*C:
        result.append(rowsat[row][col])

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
frorows collections irowsport defaultdict
def isToeplitzrowsatrix(rowsatrix):
    d = defaultdict(list)
    R=len(rowsatrix)
    C=len(rowsatrix[0])
    for i in range(R):
        for j in range(C):
            d[i-j].append(rowsatrix[i][j])
       
    for o in d.values():
        o=set(o)
        if len(o)==1:
            continue
        else:
            return False
    return True
rows=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(isToeplitzrowsatrix(rows))


frorows collections irowsport defaultdict
def rowsatrix(rowsat):
    if not rowsat or not rowsat[0]:
        return []
    
    R,C=len(rowsat),len(rowsat[0])
    dia =defaultdict(list)

    for i in range(R):
        for j in range(C):
            dia[i+j].append(rowsat[i][j])

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
    


rowsat = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(rowsatrix(rowsat))


def rowsodifiedrowsatrix(rowsatrix): 
    R=len(rowsatrix)
    C=len(rowsatrix[0])   
    for i in range(R):
        for j in range(C):
            if rowsatrix[i][j]==-1:
                rows=findGreatest(i,j,R)
                rowsatrix[i][j]=rows 
    return rowsatrix   

def findGreatest(i,j,R):
    rows=float("-inf")
    while i<R:
        rows = rowsax(rows,rowsatrix[i][j])
        i+=1
    return rows
    



rowsatrix = [[1,2,-1],[4,-1,6],[7,8,9]]
print(rowsodifiedrowsatrix(rowsatrix))


def nextGreaterElerowsent(nurowss1,nurowss2):
    rows = 0 
    res=[]
    for n in nurowss1:
        index=nurowss2.index(n)
        for nn in nurowss2[index:]:
            if nn>n:
                rows=nn
                break
            else:
                rows=-1
        res.append(rows)

nurowss1 = [4,1,2]
nurowss2 = [1,3,4,2]
print(nextGreaterElerowsent(nurowss1, nurowss2))


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



def search(nurowss,target):
    l=0
    r=len(nurowss)

    while l<=r:
        rows=l+(r-l)//2

        if nurowss[rows]==target:
            return rows
        if nurowss[rows]<target:
            l=rows+1
        else:
            r=rows-1
    return -1

#urowss = [-1,0,3,5,9,12]
nurowss = [-1,0,3,5,9,12]
target=13
print(search(nurowss, target))


nurows=[1,2,3,4]
nurows="".join(rowsap(str,nurows))
print(nurows)


def validPalindrorowse(s):
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
print(validPalindrorowse(s))


def rowsinirowsurowsLength(s):
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
print(rowsinirowsurowsLength(s))


def waysToSplitArray(nurowss):
    s = surows(nurowss)
    v=0
    res=0
    for i in range(len(nurowss)-1):
        v+=nurowss[i]
        s-=nurowss[i]            
        if v>=s:
            res+=1
    return res

nurowss = [10,4,-8,7]
print(waysToSplitArray(nurowss))


frorows collections irowsport Counter
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


def rowsaxWidthOfVerticalArea(points):
    points=sorted(points, key=larowsbda point:point[0])
    rows=float("-inf")
    for i in range(1,len(points)):
        rowsa= points[i][0]- points[i-1][0]
        rows=rowsax(rows,rowsa)
    return rows

points =[[8,7],[9,9],[7,4],[9,7]]
print(rowsaxWidthOfVerticalArea(points))


def rowsaxScore(s):
    zeros=0
    ones=s.count("1")
    res=0

    for i in range(len(s)-1):
        if s[i]=="0":
            zeros+=1
        if s[i]=="1":
            ones-=1
        res=rowsax(res,ones+zeros)
    return res
s = "011101"
print(rowsaxScore(s))

frorows collections irowsport Counter
def perrowsuteUnique(nurowss):
    c = Counter(nurowss)
    corowsb=[]
    res=[]

    def backtrack():
        if len(corowsb)==len(nurowss):
            res.append(corowsb[:])                
            
        for n in c:
            if c[n]==0:
                continue
            corowsb.append(n)
            c[n]-=1
            backtrack()
            corowsb.pop()
            c[n]+=1
    backtrack()
    return res 

nurowss = [1,1,2]
print(perrowsuteUnique(nurowss))


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


def irowsageSrowsoother(irowsg):
    row = len(irowsg)
    col = len(irowsg[0])
    res=[[0]*col for n in range(row)]

    for i in range(row):
        for j in range(col):
            s=0
            c=0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if ii<0 or ii==row or jj<0 or jj==col:
                        continue
                    s+=irowsg[ii][jj]
                    c+=1
            res[i][j]=s//c
    return res


irowsg = [[100,200,100],[200,50,200],[100,200,100]]
print(irowsageSrowsoother(irowsg))


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


def letterCorowsbinations(digits):
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "rowsno",
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
print(letterCorowsbinations(digits))



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


frorows collections irowsport Counter
def frequencySort(nurowss):
    c = Counter(nurowss)  
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


nurowss = [-1,1,-6,4,5,-6,1,4,1]
print(frequencySort(nurowss))



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


def sirowsplifyPath(path):
    stack = []
    path = path.split("/")
    for p in path:
        if stack and p == "..": # pop stack if non-erowspty
            stack.pop()
            continue

        if p not in [".", "/", "", ".."]:
            # Ignore the "p" which are no-op, 
            # but also ".." in case the stack was in previous condition. Exarowsple: "/../"
            stack.append(p)
        
    return "/" + "/".join(stack)

path ="/horowse///foo/"
#path = "/.../a/../b/c/../d/./"
print(sirowsplifyPath(path))



def search(nurowss, target):
    l=0
    r=len(nurowss)-1

    while l<r:
        rows=(l+r)//2

        if nurowss[rows]>nurowss[r]:
            l=rows+1          
        else:
            r=rows
    rowsid=l

    if rowsid==0:
        l=0
        r=len(nurowss)-1
    elif target>=nurowss[0] and target<=nurowss[rowsid-1]:
        l=0
        r=rowsid-1
    else:
        l=rowsid
        r=len(nurowss)-1

    while l<=r:
        rows=(l+r)//2
        if nurowss[rows]==target:
            return rows
        elif target<nurowss[rows]:
            r=rows-1
        else:
            l=rows+1
    return -1

nurowss = [4,5,6,7,0,1,2]
target = 0
print(search(nurowss, target))

def divideArray(nurowss,k):
    nurowss.sort()
    res=[]
    for i in range(0, len(nurowss), 3):
        if nurowss[i+2]-nurowss[i]<=k:
            res.append([nurowss[i], nurowss[i+1],nurowss[i+2]])
    return res

nurowss = [2,4,2,2,5,2]
k = 2
print(divideArray(nurowss,k))

frorows collections irowsport Counter
def findEvenNurowsbers(digits):
    dc=Counter(digits)
    res=[]

    for n in range(100,999,2):
        n=str(n)
        nc=Counter(n)
        F=True
        for i,j in nc.iterowss():
            if dc[int(i)]<j:                    
                F=False
                break
        if F:
            res.append(n)
    return res

digits = [2,1,3,0]
print(findEvenNurowsbers(digits))

frorows collections irowsport defaultdict
def isValidSudoku(board):
    rows=defaultdict(set)
    cols=defaultdict(set)
    boxes=defaultdict(set)

    for r in range(9):
        for c in range(9):
            nurows = board[r][c]
            if nurows == ".":
                continue

            box_key = (r//3,c//3)

            if nurows in rows or nurows in cols or nurows in boxes[box_key]:
                return False
            
            rows[r].add(nurows)
            cols[c].add(nurows)
            boxes[box_key].add(nurows)
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
    return surows(res)



ratings = [1,0,2]
print(candy(ratings))

def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()
    start, end = intervals[0]
    res=[]
    for s,e in intervals[1:]:
        if end>=s:
            start=rowsin(start,s)
            end=rowsax(end, e)
        else:
            res.append([start, end]) 
            start,end=s,e  
    res.append([start,end])        
    return res
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))


def rowsaxProfit(prices):
    rowsaxprofit=0
    buyprice=prices[0]
    res=[]
    for p in prices[1:]:
        if p<buyprice:
            buyprice=p
        else:
            currprofit = p-buyprice
            rowsaxprofit=rowsax(currprofit, rowsaxprofit)
            res.append(rowsaxprofit)
            rowsaxprofit=0
            buyprice=p
    print(res)
    return surows(res)
prices = [7,1,5,3,6,4]
print(rowsaxProfit(prices))





def rowsinOPeration(nurowss):
    s=[]
    res=0
    for n in nurowss:
        while s and s[-1]>n:
            s.pop()

        if n==0:
            continue

        if not s or s[-1]<n:
            res+=1
            s.append(n)
    return res

#nurowss = [1,2,1,2,1,2]
nurowss = [4,3,4,6]
print(rowsinOPeration(nurowss))



def digitSurows(s, k):    

    while len(s)>k:
        ss=""
        sf=""
        i=0      

        while i < len(s):
            srows=0
            ss=s[i:i+k]
            for ii in ss:
                srows+=int(ii)
            sf+=str(srows)
            i+=k
        s=sf
    return s
       

s = "11111222223"
k = 3

print(digitSurows(s, k))



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
    x=rowsin(res)
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



def rowsinDeletionSize(strs):
    cols = len(strs[0])
    rows=len(strs)
    rows = [[0]*cols for i in range(rows)]
    for i in range(len(strs)):
        for j in range(len(strs[i])):
            rows[i][j]= strs[i][j]
    print(rows)
   
    c=0
    
    for j in range(cols):
            i=1
            while i<rows:
                print(rows[i-1][j])
                print(rows[i][j])
                if i<rows and rows[i-1][j]<rows[i][j]:
                    i+=1
                else:
                    c+=1
                    i+=1
                    break
    return c
   

strs = ["cba","daf","ghi"]
#strs = ["a","b"]
#strs = ["zyx","wvu","tsr"]
print(rowsinDeletionSize(strs))

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



def eraseOverlapIntervals(intervals):
    intervals.sort()
    start, end = intervals[0]
    res=0
    for start_new, end_new in intervals[1:]:
        if start_new>=end:
            end=end_new
        else:
            res+=1
            end=rowsin(end,end_new)
    return res
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))


def countBinarySubstrings(s):
    res=[]
    c=0
    d=0
    for i in s:
        if i=="0":
            if d>=1:
                res.append(d)
                d=0
            c+=1
        elif i=="1":
            if c>=1:
                res.append(c)
                c=0
            d+=1
    if c:
        res.append(c)
    if d:
        res.append(d)
    r=[]
    for i in range(1,len(res)):
        x=rowsin(res[i],res[i-1])
        r.append(x)
    return surows(r)

s = "00110011"
print(countBinarySubstrings(s))

"""
"""
def rowsaxOPerations(s):
    res=0
    ones_c=0
    n=len(s)
    i=0
    while i<n:
        if s[i]=="1":
            ones_c+=1
            i+=1
        else:
            if ones_c>0:
                res+=ones_c
            
            while i<n and s[i]=="0":
                i+=1
    return res

def rowsaxOperations(s):
    cnt=0
    i=0
    res=0
    while i < len(s):
        if s[i]=="1":
            cnt+=1
            i+=1

        elif s[i]=="0":
            res+=cnt
            i+=1
            while i<len(s) and s[i]=="0":
                i+=1
    return res
s = "1001101"
print(rowsaxOperations(s))


def countAsterisks(s):
    ss=""
    su=0
    for i in s:
        if i=="|" or i=="*":
            ss+=i
    l=0
    a=0
    for ii in ss:
        if ii=="|":
            l+=1
        if ii=="*":
            a+=1
        if l==2:
            l=0
            a=0
        if l==0:
            su+=a
            a=0
    return su
#s = "yo|uar|e**|b|e***au|tifu|l"
s = "iamprogrammer"
#s = "l|*e*et|c**o|*de|"
print(countAsterisks(s))



def addDigits(num):
    su=0
    n = str(num)
    while len(n)!=1:
        su=0                    
        i=0            
        while i<len(n):
            su+=int(n[i])
            i+=1
        n=str(su)                
    return su

num = 38
print(addDigits(num))


def countBits(n):
    res=[]
    for i in range(n+1):
        
        x=bin(i)
        x=x[2:]
        c = x.count("1")
        res.append(c)
    return res
n = 2
print(countBits(n))



def secondHighest(s):
        res=set()
        for i in s:
            if i.isnumeric():                
                res.add(int(i))
        res = sorted(list(res))
        if res[-2]:
             return res[-2]
        else:
             return -1

s = "dfa12321afd"
print(secondHighest(s))



def checkIfExist(arr):
    s=set()    
    for n in range(len(arr)):
        for nn in range(n+1,len(arr)):               
            if 2*arr[n] == arr[nn] or arr[n]==arr[nn]*2:
                return True            
            
            
    return False
#arr = [10,2,5,3]
#arr=arr = [0,-2,2]
#arr = [3,1,7,11]
#arr=[7,1,14,11]
arr = [-10,12,-20,-8,15]
print(checkIfExist(arr))


def largestOddNumber(num):
    maxOdd=float("-inf")
    for i in range(len(num)-1,-1,-1):
        if int(num[i])%2==0:
            continue
        if int(num[i])%2==1:
            maxOdd=max(maxOdd,int(num[i]))
        if int(num[:i+1])%2==1:
            maxOdd=max(maxOdd,int(num[:i+1]))
    return "" if str(maxOdd) =="-inf" else str(maxOdd)
num ="10133890"
print(largestOddNumber(num))


def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(matrix[i][j])
            print(matrix[j][i])

        for i in range(n):
            matrix[i].reverse()
    print(matrix)

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))


def averageWaitingTime(customers):
    t = 0
    total_time = 0

    for start_time, end_time in customers:
        if t>start_time:
            total_time+= t-start_time
        else:
            t = start_time
        total_time += end_time
        t+=end_time
    return total_time//len(customers)

customers = [[1,2],[2,5],[4,3]]
print(averageWaitingTime(customers))


def countSubarrays(nums):
    c=0
    for i in range(len(nums)-2):
        x = (nums[i] + nums[i+2])
        if x ==nums[i+1]//2:
            c+=1
    return c
nums = [1,2,1,4,1]
print(countSubarrays(nums))

from collections import defaultdict
def maxSum(nums) -> int:
    d=defaultdict(list)
    
    for i in nums:
        m=float("-inf")
        for s in str(i):
            m = max(m,int(s))
        d[m].append(i)
    for key in d:
        d[key].sort(reverse=True)
    maxSum=-1
    for value in d.values():
        s=0
        i=0
        if len(value)==1:
            continue
        else:        
            while i<2:
                s+=value[i]
                i+=1
        maxSum=max(maxSum, s)
    print(maxSum)

    
    
#nums = [51,71,17,24,42]
nums = [2536,1613,3366,162]
print(maxSum(nums))


def countDays(days, meetings):
    meetings.sort()
    prev_end=0

    for start, end in meetings:
        start = max(start, prev_end+1)
        length = end-start+1
        days-=max(length,0)
        prev_end=max(prev_end, end)
    return days

#days = 10
#meetings = [[5,7],[1,3],[9,10]]
days=5
meetings=[[2,4],[1,3]]
print(countDays(days, meetings))


import heapq
class KthLargest:

    def __init__(self, k,nums):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap)>k:
            heapq.heappop(self.min_heap)        

    def add(self, val):
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
    
kthLargest =KthLargest(3, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2)
kthLargest.add(10)
kthLargest.add(9)
kthLargest.add(9)


import heapq
def findKthLargest(nums, k):
    heapq.heapify(nums)
    maxi = heapq.nlargest(k, nums)
    return maxi[-1]

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))


from collections import Counter
from collections import deque
import heapq
def leastInterval(tasks, n):
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()  # pairs of [-cnt, idleTime]
    while maxHeap or q:
        time += 1

        if not maxHeap:
            time = q[0][1]
        else:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time

tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks, n))


from collections import defaultdict
def subarray(nums,k):
    prefix_sum =0
    res = 0
    prefix_cnt=defaultdict(int)
    prefix_cnt[0]=1

    for n in nums:
        prefix_sum+=n
        remain = prefix_sum%k

        res+=prefix_cnt[remain]
        prefix_cnt[remain]+=1

    return res

nums=[4,5,0,-2,-3,1]
k = 5
print(subarray(nums, k))


def maxAscendingSum(nums):
    sumT=0
    m=0

    for i in range(len(nums)):
        if i < len(nums)-1 and nums[i]<nums[i+1]:
            sumT+=nums[i]
            m=max(m,sumT)
        else:
            sumT+=nums[i]
            m=max(m,sumT)
            sumT=0
    return m
nums = [10,20,30,5,10,50]
print(maxAscendingSum(nums))


def sortArrayByParityII(nums):
    even=[]
    odd=[]
    res=[]

    for i in range(len(nums)):
        if nums[i]%2==0:
            even.append(nums[i])
        elif nums[i]%2==1:
            odd.append(nums[i])
    i=0    
    while i < len(even) or i<len(odd):
        res.append(even[i])  
        res.append(odd[i]) 
        i+=1
     
    return res

nums = [4,2,5,7]
print(sortArrayByParityII(nums))


from collections import Counter
def countPalindromicSubsequence(s):
    res=set()
    left=set()
    right=Counter(s)

    for m in s:
        right[m]-=1
        for c in left:
            if right[c]>0:
                res.add((m,c))
        left.add(m)
        
    return len(res)


def countPalindromicSubsequence(s):
    if len(s)<=2:
        return 0
    
    res=0
    chara = set(s)
    for c in chara:
        first=s.find(c)
        last=s.rfind(c)

        if first!=last:
            res+=len(set(s[first+1:last]))
    return res

s = "aabca"
print(countPalindromicSubsequence(s))

def decrypt(code, k):
    N=len(code)
    res=[0]*N
    l=0
    curr_sum=0
    for r in range(N+abs(k)):
        curr_sum+=code[r%N]

        if r-l+1>abs(k):
            curr_sum-=code[l%N]
            l=(l+1)%N

        if r-l+1==abs(k):
            if k>0:
                res[(l-1)%N]=curr_sum
            elif k<0:
                res[(r+1)%N]=curr_sum
    return res
code = [5,7,1,4]
k = 3
print(decrypt(code,k))


def countConsistentStrings(allowed, words):
    allowed=set(allowed)   
    c=0
    for i in words: 
        j=0            
        for x in i:            
            if x not in allowed:
                break
            else:
                j+=1               
            if j==len(i):
                c+=1                
            
    return c
                    
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

#allowed = "abc"
#words = ["a","b","c","ab","ac","bc","abc"]
print(countConsistentStrings(allowed, words))



def findMaxAverage(nums, k):
    l=0
    sumT=0
    maxAvg=float("-inf")
    res=float("-inf")
    for r in range(len(nums)):
        sumT+=nums[r]

        if r-l+1==k:
            maxAvg=sumT/k
            res=max(maxAvg, res)
            sumT-=nums[l]
            l+=1    

    return res

nums = [-1]
k = 1
#nums = [1,12,-5,-6,50,3]
#k = 4
print(findMaxAverage(nums,k))


def numSubarraysWithSum(nums, goal):
    n=len(nums)
    c = [0]*(n+1)
    c[0]=1
    prefixSum=0
    res=0

    for n in nums:
        prefixSum+=n
        if prefixSum >= goal:
            res+=c[prefixSum-goal]
        c[prefixSum]+=1
    return res

 

nums = [1,0,1,0,1]
goal = 2

print(numSubarraysWithSum(nums,goal))


def numSubarraysWithSum(nums, goal):
    def help(x):
        if x<0:
            return 0
    
        res=0
        l=0
        currSum=0
        for r in range(len(nums)):
            currSum+=nums[r]
            while currSum > x:
                currSum-=nums[l]
                l+=1
            res+=(r-l+1)
        return res
    
    return help(goal)-help(goal-1)

def numSubarraysWithSum(nums, goal):
    def help(goal):
        if goal<0:
            return 0
    
        res=0
        l=0
        currSum=0
        for r in range(len(nums)):
            currSum+=nums[r]
            while l <= r and currSum > goal:
                currSum-=nums[l]
                l+=1
            res+=(r-l+1)
        return res
    
    return help(goal)-help(goal-1)


nums = [1,0,1,0,1]
goal = 2

#nums = [0,0,0,0,0]
#goal = 0

print(numSubarraysWithSum(nums,goal))



def maxVowels(s, k):
    vowels={"a", "e", "i", "o", "u"}
    l=0
    res=0
    c=0

    for r in range(len(s)):
        if s[r] in vowels:
            c+=1  
           
        if r-l+1 > k:
            if s[l] in vowels:
                c-=1
       
            l+=1
        res = max(res, c)
    return res

s = "abciiidef"
k = 3

#s="aeiou"
#k=2

print(maxVowels(s,k))


def maxPower(s):
    res=0
    l=0
    c=0

    for r in range(len(s)):
        cost = ord(s[r]) - ord(s[l])
        if cost==0:
            c+=1
        if cost!=0:
            while l!=r:
                l+=1
            c=1
        res=max(c, res)                
    return res
s = "leetcode"
#s = "abbcccddddeeeeedcba"
print(maxPower(s))


def canThreePartsEqualSum(arr):
    sumT=sum(arr)
    res=0
    result=[]
    x=sumT/3
    for i in arr:
        res+=i
       
        if res==x:
            result.append(1)
            res=0
        if len(result)==3:
            return True
            
    return False

arr = [1,1,1,1]
#arr = [0,2,1,-6,6,-7,9,1,2,0,1]
print(canThreePartsEqualSum(arr))


def takeCharacters(s,k):            
    l=0
    n=len(s)
    res=float("inf")
    c={"a":0,"b":0,"c":0}
    for le in s:
        c[le]+=1            
    values = min(c.values())
    if values < k:
        return -1

    for r in range(n):
        c[s[r]]-=1
        while min(c.values())<k:
            c[s[l]]+=1
            l+=1
        diff=n - (r-l+1)
        res=min(res,diff )            
    return res

s = "aabaaaacaabc"
k = 2
print(takeCharacters(s,k))

"""
def canBeEqual(target, arr) -> bool:
    x=sorted(target)
    y=sorted(arr)
    return x==y

target = [3,7,9]
arr = [3,7,11]
print(canBeEqual(target, arr))
