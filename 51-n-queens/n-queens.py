class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=[False]*n
        posdiagonal=[False]*(2*n-1)
        negdiagonal=[False]*(2*n-1)
        board=[["."]*n for i in range(n)]
        res=[]
        def backtrack(r):
            if r==n:
                res.append(["".join(row) for row  in board] )
                return
            for c in range(n):
                posd=r-c
                nevd=r+c
                if col[c] or posdiagonal[posd] or negdiagonal[nevd]:
                    continue
                col[c] = posdiagonal[posd] = negdiagonal[nevd]=True
                board[r][c]="Q"
                backtrack(r+1)
                col[c] = posdiagonal[posd] = negdiagonal[nevd]=False
                board[r][c]="."
        backtrack(0)
        return res
            
            
        

        