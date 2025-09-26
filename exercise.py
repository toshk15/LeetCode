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

"""
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