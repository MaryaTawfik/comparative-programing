from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_area=float('-inf')
        while l < r:
            w=abs(r-l)
            h=min(height[l],height[r])
            current_area=w*h
            max_area=max(max_area,current_area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            
        return max_area














        
        # left, right = 0, len(height) - 1
        # max_area = 0
        
        # while left < right:
            
        #     width = right - left
        #     h = min(height[left], height[right])
        #     max_area = max(max_area, h * width)
            
           
        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        
        # return max_area
