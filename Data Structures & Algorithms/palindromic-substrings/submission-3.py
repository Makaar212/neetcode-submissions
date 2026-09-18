class Solution:
    def countSubstrings(self, s: str) -> int:
        # Input string 
        # output the amount of continuous substrings that are palindrones
        # edge cases, empty? proper? 

        # is pali function 
        dp = {}
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in dp:
                    res += 1
                elif self.isPali(s[i: j + 1]):
                    res += 1
                    dp[s[i:j + 1]] = 1
        return res 

    def isPali(self, s):
        l,r = 0 , len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
