class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort based on the ending pos in decresing order
        point=sorted(points, key=lambda a: a[1] ) 
        # i want to check if point[r][1]>=point[l][0]
        l=0
        r=1
        arrow=0
        while l<r and r<len(point):
            if point[r][0]<=point[l][1] :
                r+=1
                continue
            
            else:
                arrow+=1
                l=r
                r+=1
        return arrow+1
