from collections import Counter
def repeatedCharacter(s):
        """
        c = Counter(s)
        print(c)
        d = set(s)
        d=list(d)
        d.sort()
        res=0
        smin=""
        idmin=float('inf')
        for i in d:            
            if c[i]>=2:
                id1 = s.find(i)
                id2 = s.find(i,id1+1)
                res = id2-id1               
                idmin = min(idmin, res)
                smin=i
        return smin
        """
       
        f = set()

        for i in s:
            if i in f:
                return i
            f.add(i)
s = "abccbaacz"
print(repeatedCharacter(s))

"""
Example 1:

Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

Example 2:

Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
 
"""