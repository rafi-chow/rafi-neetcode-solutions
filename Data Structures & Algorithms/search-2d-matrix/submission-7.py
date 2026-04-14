class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        L = 0
        R = rows * cols - 1

        while L <= R:
            mid = (L + R) // 2
            #want to access where mid is
            #if mid = 5, row 2 and col 2
            r = mid // cols #5 / 4 = 1
            c = mid % cols #5 / 3 = 1

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                L = mid + 1
            else:
                R = mid - 1
        return False