class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        
        for r in range(9):
            for c in range(9):
                spot = board[r][c]
                if spot == ".":
                    continue
                elif spot in rows[r] or spot in cols[c] or spot in squares[ r // 3, c // 3]:
                    return False
                else:
                    rows[r].add(spot)
                    cols[c].add(spot)
                    squares[r// 3, c // 3].add(spot)

        
        return True