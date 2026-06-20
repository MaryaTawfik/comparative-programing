class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        box = (row // 3, col // 3)

                        for num in "123456789":
                            if (
                                num not in rowcheck[row]
                                and num not in colcheck[col]
                                and num not in boxcheck[box]
                            ):
                                board[row][col] = num
                                rowcheck[row].add(num)
                                colcheck[col].add(num)
                                boxcheck[box].add(num)

                                if backtrack():
                                    return True

                                board[row][col] = "."
                                rowcheck[row].remove(num)
                                colcheck[col].remove(num)
                                boxcheck[box].remove(num)

                        return False

            return True


      

        rowcheck={}
        colcheck={}
        boxcheck={}
        
        for i in range(9):
            rowcheck[i]=set()
            colcheck[i]=set()
            # boxcheck[i]=set()

        for r in range(3):
            for c in range(3):
                boxcheck[(r, c)] = set()

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num= board[row][col]
                    box=(row//3 , col//3)

                    rowcheck[row].add(num)
                    colcheck[col].add(num)
                    boxcheck[box].add(num)

        backtrack()


        