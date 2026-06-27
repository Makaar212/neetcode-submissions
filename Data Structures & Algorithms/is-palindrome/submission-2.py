class Solution:
    def isPalindrome(self, s: str) -> bool:     
        if not s:
            return False
        
        alnum = ''
        for c in s:
            if c.isalnum():
                alnum += c
        

        l = 0 
        r = len(alnum) - 1

        while l < r:
            if alnum[l].lower() != alnum[r].lower():
                return False
            l += 1 
            r -= 1
        

        return True
        