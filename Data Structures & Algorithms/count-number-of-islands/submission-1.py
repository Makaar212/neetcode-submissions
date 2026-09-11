class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # Input: grid of 1's and 0's. 1 means land 0 means water. 
        # Goal: find islands
        # Ideas:
            # make a out of bounds function for quick checks, 
            # double for loop time comp allows for double for loop
            # have a check, if check met then increase a counter

            # Iterate through the grid, 
            # if you find a 1, then do dfs to find all connected lands, 
        
        seen = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r>= ROWS or c >= COLS or (r,c) in seen or grid[r][c] == "0":
                return 
            if grid[r][c] == "1":
                seen.add((r,c))
                dfs(r + 1,c)
                dfs(r - 1,c)
                dfs(r,c + 1)
                dfs(r,c - 1)

                return True
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in seen and grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        return res

