class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstr= [str(i) for i in nums]
        def merge_sort(l,r):
            if l>=r:
                return [numstr[l]]
            m=(l+r)//2
            left=merge_sort(l,m)
            right=merge_sort(m+1,r)
            return merge(left,right)
        def merge(left_arr,right_arr):
            res=[]
            i=j=0
            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]+right_arr[j]>right_arr[j]+left_arr[i]:
                    res.append(left_arr[i])
                    i+=1
                else:
                    res.append(right_arr[j])
                    j+=1
            res.extend(left_arr[i:])
            res.extend(right_arr[j:])
            return res
        res="".join(merge_sort(0,len(numstr)-1))
        return "0" if res[0]=="0" else res
                    
                
        

        
