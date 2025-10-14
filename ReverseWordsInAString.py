"""
def reverseWords(s):
    s = s.split()
    s = s[::-1]     
    return " ".join(s)


def reverseWords(s) -> str:
    ans = ""
    words = s.split()
    for i in range(len(words)-1,-1,-1):
        ans += words[i]
        if i > 0: 
            ans += " "
    return ans

s ="the sky is blue"
print(reverseWords(s))
"""

def setzeros(mat):
    row=len(mat)
    col=len(mat[0])
    si=set()
    sj=set()
    for i in range(row):
        for j in range(col):
            if mat[i][j]==0:
                si.add(i)
                sj.add(j)
    #print(si)
    #print(sj)
    for i in range(row):
        for j in range(col):
            if i in si or j in sj:
                mat[i][j]=0
    print(mat)
               
    
    
    

#mat=[[1,1,1],[1,0,1],[1,1,1]]
mat = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setzeros(mat))


