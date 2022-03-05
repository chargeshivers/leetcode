# https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])

    def _search(i, j):
        if i >= m or j < 0:
            return False

        top_right = matrix[i][j]

        if target == top_right:
            return True
        elif target < top_right:
            return _search(i, j - 1)
        else:
            return _search(i + 1, j)

    return _search(0, n - 1)
