class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rowcheck=set()
        for row in range(len(board)):
            rowcheck=set()
            for col in range(len(board)):
                if board[row][col] != ".":
                    if board[row][col] in rowcheck:
                        return False
                    
                    rowcheck.add(board[row][col])
        

        for col in range(len(board)):
            colcheck=set()
            for row in range(len(board)):
                if board[row][col] != ".":
                    if board[row][col] in colcheck:
                        return False
                    
                    colcheck.add(board[row][col])

        for row in range(0,9,3):
            for col in range(0,9,3):
                boxcheck=set()
                for r in range(row,row+3):
                    for c in range (col,col+3):

                        if board[r][c] != ".":
                            if board[r][c] in boxcheck:
                                return False
                            
                            boxcheck.add(board[r][c])

        return True





        
               


        
            

        


                
            

       
