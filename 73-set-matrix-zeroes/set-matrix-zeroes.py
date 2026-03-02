from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        place=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row=[i,j]
                    place.append(row)
                    # for k in range (len(matrix[0])):
                    #     matrix[i][k] = 0
                    # for l in range(len(matrix)):
                    #     matrix[l][j] =0
        for i in range(len(place)):
            for k in range(len(matrix[0])):
                matrix[place[i][0]][k]=0
            for l in range(len(matrix)):
                matrix[l][place[i][1]]=0

        return matrix


















        # m, n = len(matrix), len(matrix[0])
        # first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        # first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = 0
        #             matrix[0][j] = 0
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][0] == 0 or matrix[0][j] == 0:
        #             matrix[i][j] = 0
        # if first_row_zero:
        #     for j in range(n):
        #         matrix[0][j] = 0
        # if first_col_zero:
        #     for i in range(m):
        #         matrix[i][0] = 0
