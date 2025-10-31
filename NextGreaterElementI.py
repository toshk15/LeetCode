def nextGreaterElement(num1, num2):
    
    numIdx = {n:i for i, n in enumerate(num1)}
    res = [-1]*len(num1)
    """
    stack=[]
    #for i in range(len(num2)):
    for curr in num2:
        #curr = num2[i]

        while stack and curr > stack[-1]:
            val = stack.pop()
            idx = numIdx[val]
            res[idx] = curr
        
        if curr in numIdx:
            stack.append(curr)

    return res

    """

    for i in range(len(num2)):
        if num2[i] not in numIdx:
            continue

        for j in range(i+1, len(num2)):
            if num2[j] > num2[i]:
                idx = numIdx[num2[i]]
                res[idx] = num2[j]
                break

    return res


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
        return res


num1=[4,1,2]
num2=[1,3,4,2]

print(nextGreaterElement(num1, num2))

"""

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

"""