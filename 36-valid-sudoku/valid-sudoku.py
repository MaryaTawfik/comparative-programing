class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rowcheak
        for row in range(9):
            rowcheck=set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in rowcheck:
                        return False
                    rowcheck.add( board[row][col])
        #colcheack

        for col in range(9):
            colcheack=set()
            for row in range(9):
                if board[row][col]!= ".":
                    if board[row][col] in colcheack:
                        return False
                    colcheack.add(board[row][col])



        for row in range(0,9,3):
            for col in range(0,9,3):
                boxcheack=set()
                for r in range(row,row+3):
                    for c in range(col,col+3):
                        if board[r][c]!= ".":
                            if board[r][c] in boxcheack:
                                return False
                            boxcheack.add(board[r][c])
        return True





        # 0,0 0,1 0,2
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2

        # 0,3 0,4 0,5
        # 1,3 1,4 1,5
        # 2,3 2,3 2,4


       


































        # # rowcheck=set()
        # for row in range(len(board)):
        #     rowcheck=set()
        #     for col in range(len(board)):
        #         if board[row][col] != ".":
        #             if board[row][col] in rowcheck:
        #                 return False
                    
        #             rowcheck.add(board[row][col])
        

        # for col in range(len(board)):
        #     colcheck=set()
        #     for row in range(len(board)):
        #         if board[row][col] != ".":
        #             if board[row][col] in colcheck:
        #                 return False
                    
        #             colcheck.add(board[row][col])

        # for row in range(0,9,3):
        #     for col in range(0,9,3):
        #         boxcheck=set()
        #         for r in range(row,row+3):
        #             for c in range (col,col+3):

        #                 if board[r][c] != ".":
        #                     if board[r][c] in boxcheck:
        #                         return False
                            
        #                     boxcheck.add(board[r][c])

        # return True





        
               


        
            

        


                
            

       
