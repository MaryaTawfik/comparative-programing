# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         row=len(mat)
#         col=len(mat[0])
#         res=[]
#         c_row=0
#         c_col=0
#         up=True
#         while len(res)<row*col:
#             if up:
#                 while c_row>=0 and c_col>col:
#                     res.append(mat[c_row][c_col])
#                     c_col+=1
#                     c_row-=1
#                     if c_col==col:
#                         c_col-=1
#                         c_row+=2
#                     else:
#                         c_row+=1
#                         up=False
#             else:
#                 while c_col>=0 and c_row<row:
#                     res.append(mat[c_row][c_col])
#                     c_col-=1
#                     c_row+=1
#                     if c_row==row:
#                         c_col+=2
#                         c_row-=1
#                     else:
#                         c_col-=1
#                     up=True
#         return res



class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        res = []
        r = c = 0
        up = True

        while len(res) < row * col:
            if up:
                while r >= 0 and c < col:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
                # Adjust position after reaching boundary
                if c >= col:
                    c = col - 1
                    r += 2
                elif r < 0:
                    r = 0
                up = False
            else:
                while c >= 0 and r < row:
                    res.append(mat[r][c])
                    r += 1
                    c -= 1
                # Adjust position after reaching boundary
                if r >= row:
                    r = row - 1
                    c += 2
                elif c < 0:
                    c = 0
                up = True
        return res

            
