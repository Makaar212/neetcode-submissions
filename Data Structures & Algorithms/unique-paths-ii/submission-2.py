class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # editing in place

        # changing all of the obstacles to -1 
        # editing first row and col to equal 1 until we run into an obstacle

        # iterate through the rest of the cells and add up the left and top as long as they're not
        # obstacles

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0

        grid = obstacleGrid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = -1

        r = 0
        while r < ROWS and grid[r][0] != -1:
            grid[r][0] = 1
            r += 1
        c = 0
        while c < COLS and grid[0][c] != -1:
            grid[0][c] = 1
            c += 1


        for r in range(1, ROWS):
            for c in range(1, COLS):
                # if obstacle
                if grid[r][c] == -1:
                    continue


                if grid[r][c - 1] != -1:
                    grid[r][c] += grid[r][c - 1]
                if grid[r -1][c] != -1:
                    grid[r][c] += grid[r - 1][c]

        return grid[ROWS - 1][COLS - 1]
