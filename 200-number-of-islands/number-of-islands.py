class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def bound(r,c):
            return r<0 or c<0 or r>=rows or c>=cols
        count=1
        def dfs(r,c):
            if bound(r,c):
                return 
            if grid[r][c]=="0":
                return 
            # if bound(r,c):
            #     return 1
            grid[r][c]="0"
            for dr,dc in directions:
                # count+=1
                dfs(r+dr,c+dc)
        count=0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    dfs(row,col)
                    count+=1
        return count