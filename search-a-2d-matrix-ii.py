class Solution:
    def searchMatrix(self, matrix, target):

        rows, cols = len(matrix), len(matrix[0])

        top_right = matrix[0][cols - 1]
        bottom_left = matrix[rows - 1][0]
        row_inc, col_inc = 0, 0

        while True:
            if target > top_right and target < bottom_left:
                try:
                    row_inc += 1
                    top_right = matrix[row_inc][cols - 1 - col_inc]
                    bottom_left = matrix[rows - 1 - row_inc][col_inc]
                except IndexError:
                    return False

            if target < top_right:
                try:
                    col_inc += 1
                    top_right = matrix[row_inc][cols - 1 - col_inc]
                except IndexError:
                    return False

            if target > bottom_left:
                try:
                    col_inc += 1
                    bottom_left = matrix[rows - 1 - row_inc][col_inc]
                except IndexError:
                    return False

            if top_right == target or bottom_left == target:
                return True