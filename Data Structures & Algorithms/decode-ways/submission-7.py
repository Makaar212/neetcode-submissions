class Solution:
    def numDecodings(self, s: str) -> int:
        # input string of digits
        # output the amount of ways that the digits can be re arranged

        # Observations
            # we can either take one digit, or two digits
                # One: must not be 0
                # two: must either start with 1 or start with 2 AND second digit between 0-6
        # base case: when i= len (s)

        dp = {len(s): 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == '2' and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i]= dp[i + 1]
                if (i + 1 < len(s) and (s[i] == "1" or (s[i] == '2' and s[i + 1] in "0123456"))):
                    dp[i] += dp[i + 2]
        return dp[0]
            