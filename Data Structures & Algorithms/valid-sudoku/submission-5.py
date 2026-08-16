class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if item == '.':
                    row[r].add(item)
                    col[c].add(item)
                    squares[r//3, c//3].add(item)
                elif item not in row[r] and item not in col[c] and item not in squares[r//3, c//3]:
                    row[r].add(item)
                    col[c].add(item)
                    squares[r//3, c//3].add(item)
                else:
                    return False
        
        return True