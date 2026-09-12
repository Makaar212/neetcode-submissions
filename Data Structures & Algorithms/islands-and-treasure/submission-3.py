class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # for the bfs solution we could use a multi source bfs, the reason why we would need
        # multisource is becasue we want to be able to mark visited from multiple sources of the gates at the same time
        # if we have already visited a position then don't update, 

        # from gate Run bfs

        # Algo:

        # For every element in grid
            # if element is a gate, run bfs
                # from gate start going in every direction and mark them as distance IF it's not water or 
                # it hasn't been visited
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        seen = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def bfs():
            
            distance = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == -1 or(row,col) in seen:
                        continue
                    seen.add((row,col))
                    grid[row][col] = distance

                    for dr, dc in directions:
                        q.append((row + dr, col + dc))
                distance += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        bfs()