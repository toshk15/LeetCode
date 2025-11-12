class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
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
        res2=[]
        for i,j in res:
            if j==x[1]:
                res2.append(i)
 
        return res2
       

"""
Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".

Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".
"""