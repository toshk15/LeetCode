class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballons="balloon"   
        count={}       

        for i in text:
            if i in ballons:
                count[i]=count.get(i,0)+1     
        i=0
        res=[]
        F=True
        while F:
            s=""
            while i < len(ballons):
                if not count.get(ballons[i],0) > 0:
                    F=False              
                    break
                s+=ballons[i]
                count[ballons[i]]-=1
                if count[ballons[i]] == 0:
                    F=False
                i+=1       
            if s == ballons:     
                res.append(s)   
            i=0        
    
        return len(res)
    
"""
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_freq = Counter(text) # {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}, considering the text = 'balloon'

        b_count = balloon_freq['b'] # 1
        a_count = balloon_freq['a'] # 1
        l_count = balloon_freq['l']//2 # 1
        o_count = balloon_freq['o']//2 # 1
        n_count = balloon_freq['n'] # 1

        return min(b_count, a_count, l_count, o_count, n_count)
"""
    

"""
Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

"""