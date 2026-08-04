class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Creates a transposed board
        board_t = [[] for _ in range(9)]
        # Checks duplicates per row
        for row in board:
            seen = set()
            for i in range(len(row)):
                board_t[i].append(row[i])
                if row[i] in seen:
                    return False
                elif row[i] != '.':
                    seen.add(row[i])
                
        # Checks duplicates per column
        for col in board_t:
            seen = set()
            for i in range(len(col)):
                if col[i] in seen:
                    return False
                elif col[i] != '.':
                    seen.add(col[i])
        
        # Checks duplicates per 3x3 sub-box
        map = defaultdict(set)
        for rownum, row in enumerate(board):
            for i in range(len(row)):
                if row[i] in map[(rownum//3, i//3)]:
                    return False
                elif row[i] != '.':
                    map[(rownum//3, i//3)].add(row[i])

        
        return True