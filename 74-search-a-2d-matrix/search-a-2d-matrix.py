class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        #let first find the correct row then we will try to find the corrct col
        #mid=(left+right)//2  mid of row
        # if target <matrix[mid] and target<matrix[mid-1][0]:
        #     right=mid
        # if  target <matrix[mid] and target>matrix[mid-1][0]:
        #     the neede row is find
        #     then we will try to find the element based on the colomun by using normal bynary search
        # if target >matrix[mid] and target<matrix[mid+1][0]:
        #     left=mid
        # if target >matrix[mid] and target>matrix[mid-1][0]:
        #      then we will try to find the element based on the colomun by using normal bynary search
        left=0
        right= len(matrix)-1
        # lc=0
        # rc=len(matrix[0])-1
        while left <= right:
            mid=(left+right)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                lc=0
                rc=len(matrix[0])-1
                while lc<=rc:
                    m=(lc+rc)//2
                    if matrix[mid][m]==target:
                        return True
                    elif matrix[mid][m]<target:
                        lc=m+1
                    else:
                        rc=m-1
                return False
            elif target <matrix[mid][0]:
                right=mid-1
            else:
                left=mid +1
        return False
