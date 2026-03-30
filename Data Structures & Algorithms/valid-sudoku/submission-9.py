class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        for row in board:
            rows.clear()
            for i in row:
                if i == ".":
                    continue
                elif i.isalnum():
                    if i in rows:
                        return False
                    rows.add(i)
                else:
                    continue

        columns = set()
        for c in range(9):
            columns.clear()
            for r in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                elif value.isalnum():
                    if value in columns:
                        return False
                    columns.add(value)
                else:
                    continue
        box = set()
        for c in range(0, 9, 3):
            for r in range(0, 9, 3):
                box.clear()
                for i in range(3):
                    for j in range(3):
                        value = board[j + r][i + c]
                        if value == ".":
                            continue
                        elif value.isalnum():
                            if value in box:
                                return False
                            box.add(value)
                        else:
                            continue
        return True

