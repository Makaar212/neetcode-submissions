class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # observing that there is only one way to get to the first column and row

        dp = [[1] * n for i in range(m)]
        
        ROWS, COLS = m, n

        for r in range(1, ROWS):
            for c in range(1, COLS):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        return dp[ROWS - 1][COLS - 1]