class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # similar to how you would do it by hand, 

        # base cases, is this the right letter, is this out of bounds, is our current word greater
        # then the length of the other word
        # is 
        # constraints is we can't use the same element
        ROWS = len(board)
        COLS= len(board[0])
        path = set()
        def dfs(r,c, i): 
            if i == len(word):
                return True
            if (r < 0 or c < 0 or c >= COLS or r >= ROWS or (r,c) in path or i >= len(word) or word[i] != board[r][c]):
                return 
            
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c- 1, i + 1))
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False