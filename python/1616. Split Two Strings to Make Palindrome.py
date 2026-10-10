class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def make_pa(s1,s2):
            l=0
            r=len(s2)-1
            while l<=r and s1[l]==s2[r]:
                r-=1
                l+=1
            return (l>=r) or is_palindrome(s1,l,r) or is_palindrome(s2,l,r)
            
        def is_palindrome(s,l,r):
            pa=s[l:r+1]
            return pa==pa[::-1]
        return make_pa(a,b) or make_pa(b,a)
