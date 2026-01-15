class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        if len(arr)<m*k:
            return False
        c=0
        for i in range(m,len(arr)):
            if arr[i]==arr[i-m]:
                c+=1
            else:
                c=0
            if c>=(k-1)*m:
                return True
        return False
        
            
    
                
        
        
        
        
