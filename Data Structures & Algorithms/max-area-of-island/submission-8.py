class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # dfs 
        # for every area of land run dfs on it
            # for this land check up right down left,
            # if there is a piece of land, mark total distance up 1
            # return cur distance

        # base case, out of bounds or water

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set()
        area = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in seen:
                return 0
            nonlocal area
            seen.add((r,c))
            for dr, dc in directions:
                area = max(area, 1 + dfs(r + dr, c + dc))
            return area
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = 0
                    res = max(res, dfs(r, c))
        return res
            
            
        