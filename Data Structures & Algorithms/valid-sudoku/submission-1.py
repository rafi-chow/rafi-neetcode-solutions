from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        #iterate over each row, see if duplicate
        for row in board:
            rows.clear()
            for val in row:
                if val == ".":
                    continue
                if val in rows:
                    return False
                rows.add(val)

        for c in range(9):
            columns.clear()
            for r in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in columns:
                    return False
                columns.add(val)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = set()
                for r in range(3):
                    for c in range(3):
                        val = board[box_row + r][box_col + c]
                        if val == ".":
                            continue
                        if val in box:
                            return False
                        box.add(val)
        return True