class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # this seems like a multi source bfs question 
        # what we can do is go through the list and see how many fresh fruit there is, then we subtract
        # from that number every time we mold a fresh fruit

        # to do multi source bfs, we should go through the whole grid
        # if cell is 0 ignore, if cell is 1 increment fresh fruit counter
        # if cell is 2 add it to the q to start the multi source bfs

        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        q = deque()
        seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
        if not q and not fresh:
            return 0
        
        def addCell(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen 
                or grid[r][c] == 0 or grid[r][c] == 2):
                return 
            nonlocal fresh
            fresh -= 1
            q.append((r,c))
            seen.add((r,c))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()               
                addCell(r + 1,c)
                addCell(r - 1,c)
                addCell(r,c + 1)
                addCell(r,c - 1)

            minutes += 1

        print(fresh)
        print(minutes)
        return minutes - 1 if fresh <= 0 else -1
        # while q:
            # for _ in range(q):
                # if node is out of bounds or is 0 or is seen already, continue

                # else add cords of up right down left to q

            # increase minutes by 1 
        

        # return minutes if there is no fresh fruit

    

        