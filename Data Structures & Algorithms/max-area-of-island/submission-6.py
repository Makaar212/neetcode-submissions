class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # do bfs




        # Just like in # islands we are gong to go to ever single point, 
        # if it's a 1 run bfs on it and sink the island
        directions = [[-1, 0], [1,0], [0, 1], [0,-1]]
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            curArea  = 0

            while q:
                r, c = q.popleft()

                if r < 0 or c < 0 or c >= COLS or r >= ROWS or grid[r][c] == 0:
                    continue
                
                grid[r][c] = 0
                curArea += 1

                for dr, dc in directions:
                    q.append((r + dr, c + dc))
            
            return curArea




        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(bfs(r,c), res)

        return res