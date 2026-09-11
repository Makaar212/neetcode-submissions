class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # couple of things here

        # Create an isPalindrome function

        # every function needs to be seperated into sub strings can filter afterwards
        # backtracking portion here, 

        # base case: if total length > len str return, if i > len s return if 
        

        # Use backtracking to split into substrings, then check palindromes for filters for every list

        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res

        
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        l, r = i, j

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        