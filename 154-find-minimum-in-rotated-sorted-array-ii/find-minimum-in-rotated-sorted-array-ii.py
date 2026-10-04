class Solution:
    def findMin(self, nums: list[int]) -> int:
        left , right = 0, len(nums)-1
        zmin=float(inf)
        while  right < len(nums) and left <= right:
            mid = (left + right)//2
            if nums[mid] > nums[right] :
                zmin =min(nums[right] , zmin)
                left = mid +1
            elif nums[mid] == nums[right]:
                right -= 1
                zmin = min(zmin,nums[right],nums[left])
            
            elif nums[mid] < nums[right] :
                zmin = min(nums[mid], zmin)
                right = mid -1

        return zmin
        