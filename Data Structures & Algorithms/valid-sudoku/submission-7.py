from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        #rows
        for row in board:
            rows.clear()
            for val in row:
                if val == ".":
                    continue
                elif val in rows:
                    return False            
                rows.add(val)

        #columns
        for c in range(9):
            columns.clear()
            for r in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                elif value in columns:
                    return False
                columns.add(value)

        #3x3
        box = set()
        for box_col in range(0,9,3):
            for box_row in range(0,9,3):
                box.clear()
                for c in range(3):
                    for r in range(3):
                        value = board[box_col + c][box_row + r]
                        if value == ".":
                            continue
                        elif value in box:
                            return False
                        box.add(value)

        return True