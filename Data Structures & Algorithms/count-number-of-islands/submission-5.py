class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # do bfs
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        # first iterate through the grd
        # if we have a "1" then run bfs and sink that island, total += 1
        directions = [[-1, 0], [1,0], [0, -1], [0, 1]]
        def bfs(r,c):
            
            q = deque()
            q.append((r, c))

            while q:
                r, c = q.popleft()
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                    continue 
                
                grid[r][c] = "0"
                for dr, dc in directions:
                    q.append((r + dr, c + dc))


        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands