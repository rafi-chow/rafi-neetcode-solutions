from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        for row in board:
            rows.clear()
            for value in row:
                if value == ".":
                    continue
                if value in rows:
                    return False
                rows.add(value)

        for i in range(9):
            columns.clear()
            for k in range(9):
                if board[k][i] == ".":
                    continue
                if board[k][i] in columns:
                    return False
                columns.add(board[k][i])

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = set()
                for r in range(3):
                    for c in range(3):
                        value = board[box_row + r][box_col + c]
                        if value == ".":
                            continue
                        if value in box:
                            return False
                        box.add(value)

        return True