class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # base cases: ran out of bounds, found the word, len of cur > word

        # decision 1: go down
        # decision 2: go left
        # decision 3: go up
        # decision 4: go right

        # we can only check safe paths just like in valid parenth,
        # after every go, pop
        #

        res = False
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0  # left & up bounds
                or c >= len(board[0])
                or r >= len(board)  # right and down b ounds
                or i >= len(word)
                or word[i] != board[r][c]  # wrong letter
                or (r, c) in path
            ):  # or we've seen before
                return False
            path.add((r, c))
            res = dfs(r, c + 1, i + 1) or dfs(r + 1, c, i + 1   ) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r,c))

            return res


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False 
