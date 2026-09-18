class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # for every c in s
            # start checking palindromes from middle 
            # check how much each c can grow and still remain as a palidrome
        resStr = ""
        for i in range(len(s)):
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if len(s[l:r + 1]) > len(resStr):
                    resStr = s[l: r + 1]
                l -= 1
                r += 1
            l,r = i, i +1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if len(s[l: r + 1]) > len(resStr):
                    resStr = s[l:r + 1]
                l -= 1
                r += 1
        return resStr 
                