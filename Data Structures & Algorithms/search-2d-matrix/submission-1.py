class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            L = 0
            R = len(m) - 1
            while L <= R:
                mid = (L + R) // 2
                if m[mid] == target:
                    return True
                elif m[mid] < target:
                    #1 2 4 8 10
                    L = mid + 1
                elif m[mid] > target:
                    R = mid - 1
        return False