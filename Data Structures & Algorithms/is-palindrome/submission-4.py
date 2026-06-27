class Solution:
    def isPalindrome(self, s: str) -> bool:     
        if not s:
            return False
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            r -= 1
            l += 1

        return True