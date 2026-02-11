class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[]
        nums1=set(nums1)
        nums2=set(nums2)
        ans.append(list(nums1 - nums2))
        ans.append(list(nums2 - nums1))
        return ans
        