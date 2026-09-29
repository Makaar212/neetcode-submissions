class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        seen = set()
        def inRange(r, c):
            return r < ROWS and c < COLS and c >= 0 and r >= 0

               

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res += 4
                    for dr, dc in directions:
                        if inRange(r + dr, c + dc) and grid[r + dr][c + dc] == 1:
                            res -= 1
                    
        return res