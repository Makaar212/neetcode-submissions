class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # base cases: we are not on the right word, we are out of bounds, current word is bigger than last word and i is greater than word length
        # constraints: every coord can only be used once
        ROWS = len(board)
        COLS = len(board[0])

        path = set()

        def dfs(r, c, i):  # i is there to keep track of what part of the word we are on
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or i > len(word)
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return
            
            print(board[r][c])

            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res
            

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
