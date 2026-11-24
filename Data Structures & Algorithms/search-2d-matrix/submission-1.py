class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        if m == 0:
            return False

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid // n][mid % n] 

            if mid_element == target:
                return True
            elif mid_element > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
        