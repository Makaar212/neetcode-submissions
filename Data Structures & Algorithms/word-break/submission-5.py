class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = {}
        def dfs(i):
            if i == len(s):
                return True

            if i > len(s):
                return False
            if i in dp:
                return dp[i]
            res = False
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    res = max(dfs(i + len(word)), res)
            dp[i] = res
            return res
        return dfs(0)