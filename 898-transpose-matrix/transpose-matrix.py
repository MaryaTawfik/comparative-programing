class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=[]
        row=len(matrix)
        column=len(matrix[0])
        
        for i in range(column):
            n=[]
            for j in range(row):
                n.append(matrix[j][i])
            m.append(n)
        return m
        