class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # Ideas. similar to number of islands I think it's important to run dfs again
        # this time with another input which would be current area,
        # while looking for parterns we will check if current area is greater than old area,
        # at the end return area

        # goal: return max area
        # input: land and water represented with 1s and 0s on a grid

        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        cur = 0
        def dfs(r, c):
            if r < 0 or c < 0 or c >= COLS or r >= ROWS or grid[r][c] == 0:
                return

            nonlocal maxArea
            nonlocal cur 
            cur += 1
            maxArea = max(maxArea, cur)
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    cur = 0
                    dfs(r, c)
        return maxArea
