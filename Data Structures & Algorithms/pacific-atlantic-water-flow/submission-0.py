class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # this is a dfs questions, 
        res = []
        part = []
        ROWS, COLS = len(heights), len(heights[0])
        


        def pacific(r,c, water, path):
            if r < 0 or c < 0:
                return True
            if r >= ROWS or c >= COLS or heights[r][c] > water or (r,c)in path:
                return False
            path.add((r,c))
            water = heights[r][c]
            return (pacific(r + 1, c, water, path) or pacific(r - 1, c, water, path) 
                    or pacific(r , c + 1, water, path) or pacific(r, c - 1, water, path))
            

        def atlantic(r,c, water, path):                  
            if r >= ROWS or c >= COLS:
                return True
            if r < 0 or c < 0 or heights[r][c] > water or (r,c) in path:
                return False
            path.add((r,c))
            water = heights[r][c]
            return (atlantic(r + 1, c, water, path) or atlantic(r - 1, c, water, path) or 
                    atlantic(r , c + 1, water, path) or atlantic(r, c - 1, water, path))
    

        # for every elemetn in the matrix
        for r in range(ROWS):
            for c in range(COLS):
                # run dfs on it
                if pacific(r,c, heights[r][c], set()) and atlantic(r,c, heights[r][c], set()):
                    res.append([r, c]) 

        # return res
        return res
        