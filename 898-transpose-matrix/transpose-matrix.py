class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        rows,cols=len(matrix),len(matrix[0])
        for c in range(cols):
            row=[]
            for r in range(rows):
                row.append(matrix[r][c])
            ans.append(row)
        return ans
            
       