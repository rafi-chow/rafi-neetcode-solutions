class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix[0]) #4 #2
        columns = len(matrix) #3 #1

        L = 0
        R = rows * columns - 1 #11 #1

        while L <= R:
            mid = (L + R) // 2 #11 / 2 = 5 #) 1 // 2 = 0
            r = mid // rows #5/3 = 1 #0/1 = 0
            c = mid % rows #5 % 3 = 2 #0% = 0
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                R = mid - 1
            else:
                L = mid + 1
        return False