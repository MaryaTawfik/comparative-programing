class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        left = 0
        right = len(matrix) - 1

        # STEP 1: find the correct row
        while left <= right:
            mid = (left + right) // 2

            # check if target is inside this row range
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                
                # STEP 2: binary search in that row
                lc = 0
                rc = len(matrix[0]) - 1

                while lc <= rc:
                    m = (lc + rc) // 2

                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        lc = m + 1
                    else:
                        rc = m - 1

                return False

            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        return False