class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Robot can start on a 1 

        # it can be a rectangle 

        # not guarenteed path to the end


        # more optimal solution 
        if obstacleGrid[0][0] == 1:
            return 0
        cache = {}
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c):
            if r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            res =  dfs(r + 1, c) + dfs(r, c + 1)
            cache[(r,c)] = res
            return res
        return dfs(0,0)
            
            