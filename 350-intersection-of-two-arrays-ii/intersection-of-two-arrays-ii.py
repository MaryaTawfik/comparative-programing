from collections import Counter 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m=[]
        c1=Counter(nums1)
        c2=Counter(nums2)
        for i in c1:
            if i in c2:
                m.extend([i] * min(c1[i], c2[i]))
        return m
        


             

       

        
          

    
        