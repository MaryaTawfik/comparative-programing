class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col=len(matrix[0])
        row=len(matrix)
        top , bot = 0 , row-1
        pos=0
        while top <= bot:
            mid = (top + bot)//2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                pos=mid
                break
            if matrix[mid][-1] <= target:
                top = mid+1
            if matrix[mid][-1]>= target:
                bot = mid-1
        else:
            return False

        left,right=0,col-1
        while left <= right:
            mid = (left + right)//2
            if matrix[pos][mid] == target:
                return True
            if matrix[pos][mid] < target:
                left = mid+1
            elif matrix[pos][mid] > target:
                right = mid -1
        return False

        