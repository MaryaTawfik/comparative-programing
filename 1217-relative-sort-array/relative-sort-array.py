# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # res=[]
        # p1=0
        # p2=0
        # arr1.sort()
        # while p1<len(arr1) and p2<len(arr2):
            
        #     if arr1[p1]==arr2[p2]:
        #         res.append(arr1[p1])
        #         p1+=1
        #     elif arr1[p1]<arr2[p2]:
        #         p1+=1
        #     else:
        #         p1+=1
        #         p2+=1
            
            
        # return res

        # arr1_count=defaultdict(int)
        # return arr1_count
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Step 1: Create a frequency map for arr1
        count = defaultdict(int)
        for num in arr1:
            count[num] += 1

        # Step 2: Add elements from arr2 in the correct order
        result = []
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]  # Remove from map once used

        # Step 3: Add remaining elements sorted in ascending order
        remaining = sorted(count.keys())
        for num in remaining:
            result.extend([num] * count[num])

        return result
